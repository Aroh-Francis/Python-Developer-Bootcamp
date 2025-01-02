
from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
application=Flask(__name__)

@application.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course by Francis Aroh</H1></html>"

@application.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@application.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!, good to see you again'
    return render_template('form.html')


if __name__=="__main__":
    application.run(debug=True)