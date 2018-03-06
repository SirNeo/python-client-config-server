import json
import requests
from flask import make_response
from ATCException import ATCException

default_config_server = 'http://localhost:8888'

def EnableAutoConfiguration(app, appname, profile, config_server=None):
    if not config_server:
        config_server = default_config_server

    try:
        properties = requests.get('/'.join((config_server, appname, profile))).json()
        app.config.update(properties.get('propertySources')[0].get('source'))
        
    except requests.exceptions.ConnectionError:
        raise ATCException('Connection Error in EnableAutoConfiguration. URL: %s' % config_server)

    @app.route('/env')
    def env():
        resp = make_response(json.dumps(dict([(k, app.config[k]) for k in app.config['__spring_config_keys']])))
        resp.headers['Content-Type'] = 'application/json'
        return resp

