import datetime
import json
from functools import wraps
# import jwt
# from jwt.algorithms import get_default_algorithms
import pandas as pd
from flask import request, jsonify, Blueprint
# from gen_config.read_config import read_json_config
# from controller.api_connector import Authorization
# from controller.read_configs import read_json_config
# from service.get_classification_service import get_classification
# from service.reduce_dimension_service import reduce_dimen
from utils.constants import AUTH_VALIDATION_TIME
from workflow.data_pipeline_workflow import data_training_workflow,data_testing_workflow

api = Blueprint('find-yourself', __name__, url_prefix='/v1')

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers['access-token']
#         if not token:
#             return jsonify({'ERROR': 'Access token is missing'})
#         try:
#             config = read_json_config()
#             jwt.decode(token, config['flask']['key'], options={"verify_signature": False})
#         except:
#             return jsonify({'ERROR': 'Invalid token'})
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# @api.route('/login')
# def login():
#     get_default_algorithms()
#     config = read_json_config()
#
#     auth = request.authorization
#     authenticate = Authorization().authorization(auth.username, auth.password)
#     if authenticate:
#         token = jwt.encode({'user': auth.username,
#                             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=AUTH_VALIDATION_TIME)},
#                            config['flask']['key'])
#         return jsonify({'token': token})
#     return jsonify({'ERROR': 'invalid authentication'})

@api.get('/test')
def test_api():
    return jsonify({'status': 'success'})

@api.get('/training')
def get_training():
    data_training_workflow()
    return jsonify({'status': 'success'})

@api.get('/testing')
def get_testing():
    genome_test=pd.read_csv("workflow/services/external_data/genome_test.csv")
    data_testing_workflow(genome_test)
    return jsonify({'status': 'success'})    
