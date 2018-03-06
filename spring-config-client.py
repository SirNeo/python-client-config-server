from flask import Flask
from springboot import EnableAutoConfiguration
from os import getenv
from ATCException import ATCException

app = Flask(__name__)

try:
    EnableAutoConfiguration(app, appname='config-python', profile='production', config_server=getenv('CONFIG_SERVER', None))   
except ATCException as e:
    print(e)
    app.config.from_pyfile('config.yaml', silent=True) 

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
    
    print('SECRET_KEY: %s' % app.config.get('SECRET_KEY'))
    #app.run(host=conf.get('HOST'), port=int(conf.get('PORT')), debug=app.debug)
    
    app.run()
