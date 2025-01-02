from flask import Flask
'''
We initalize the Flask application by creating an instance of the Flask class. 
This will be our WSGI application.

The first argument is the name of the application’s module or package. 
If you are using a single module (as in this example), 
you should use __name__ because depending on if it’s started as application or imported
 as module the name will be different ('__main__' versus the actual import name). 
 This is needed so that Flask knows where to look for templates, static files, and so on.
  
'''
# WSGI application
application = Flask(__name__)


#To create a route, we use the route() decorator.
#The route() decorator tells Flask what URL should trigger the function.
@application.route('/') #Default route (home page)
def hello_world():
    return 'Hello, world!, Welcome to Francis Flask Application'


@application.route('/index') #Route to the index page
def index():
    return 'This is my index page'

@application.route('/contact') #Route to the contact page
def contact():
    return 'This is my contact page'


#Entry point of the application
if __name__ == '__main__':
    application.run(debug=True) #Run the application in debug mode. Auto updates the server when changes are made.

