import datetime
import json
from functools import wraps
import pandas as pd
from flask import request, jsonify, Blueprint
from workflow.data_pipeline_workflow import data_training_workflow,data_testing_workflow

api = Blueprint('find-yourself', __name__, url_prefix='/v1')

###### FUTURE WORK #############

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
###### FUTURE WORK #############

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
