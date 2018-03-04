from flask import Flask
from springboot import EnableAutoConfiguration
from os import getenv

app = Flask(__name__)

EnableAutoConfiguration(app, appname='config-python', profile='production', config_server=getenv('CONFIG_SERVER', None))

#FUNCIONA
#app.config.from_pyfile('config.yaml', silent=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    # CONFIG: app.config.get('propertySources')[0]
    # SERVER_NAME = app.config.get('propertySources')[0].get('source').get('SERVER_NAME')
    HOST = app.config.get('propertySources')[0].get('source').get('HOST')
    PORT = int(app.config.get('propertySources')[0].get('source').get('PORT'))
    app.debug = app.config.get('propertySources')[0].get('source').get('DEBUG')
    print(app.config.get('propertySources')[0])
    print(app.config.get('propertySources')[0].get('source').get('HOST'))    
    
    app.run(host=HOST, port=PORT, debug=app.debug)
