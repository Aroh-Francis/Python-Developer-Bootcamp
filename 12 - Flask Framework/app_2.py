from flask import Flask


application = Flask(__name__)



@application.route('/') 
def hello_world():
    return 'Hello, world!, Welcome to Francis Flask Application'


@application.route('/index') 
def index():
    return 'This is my index page'

@application.route('/contact') 
def contact():
    return 'This is my contact page'



if __name__ == '__main__':
    application.run(debug=True) 

