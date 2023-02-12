from flask import Flask

from controller.api import api

flask_app = Flask('findyourself')
flask_app.register_blueprint(api)
# flask_app.register_blueprint(monitering)

# def list_route(flaskapp):
#     return ['%s' % rule for rule in flaskapp.url_map.iter_rules()]

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8088, debug=True)