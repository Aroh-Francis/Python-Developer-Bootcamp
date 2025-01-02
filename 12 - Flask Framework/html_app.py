from flask import Flask, render_template


application = Flask(__name__)



@application.route('/') 
def hello_world():
    return "<html><H1>This is Flask Web Framework Tutorial by Francis Aroh!</H1></html>"


@application.route('/index') 
def index():
    return render_template('index.html') 
                           

@application.route('/about') 
def about():
    return render_template('about.html')



# @application.route('/contact') 
# def contact():
#     return 'This is my contact page'



if __name__ == '__main__':
    application.run(debug=True) 

