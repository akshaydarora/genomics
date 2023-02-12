import datetime
import json
from functools import wraps
import jwt
from jwt.algorithms import get_default_algorithms

from flask import request, jsonify, Blueprint

# from configs.read_config import read_json_config
from controller.api_connector import Authorization
from controller.read_configs import read_json_config
from utils.constants import AUTH_VALIDATION_TIME

api = Blueprint('find-yourself', __name__, url_prefix='/v1')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['access-token']
        if not token:
            return jsonify({'ERROR': 'Access token is missing'})
        try:
            config = read_json_config()
            jwt.decode(token, config['flask']['key'], options={"verify_signature": False})
        except:
            return jsonify({'ERROR': 'Invalid token'})
        return f(*args, **kwargs)

    return decorated


@api.route('/login')
def login():
    get_default_algorithms()
    config = read_json_config()

    auth = request.authorization
    authenticate = Authorization().authorization(auth.username, auth.password)
    if authenticate:
        token = jwt.encode({'user': auth.username,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=AUTH_VALIDATION_TIME)},
                           config['flask']['key'])
        return jsonify({'token': token})
    return jsonify({'ERROR': 'invalid authentication'})


@api.get('/test')
def test_api():
    return jsonify({'status': 'success'})
