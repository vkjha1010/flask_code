"""
    program to use the url_for() and redirect() for URL Building
"""

from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/hello/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/hello/<guest>')
def hello_guest(guest):
    return 'Hello %s' %guest

@app.route('/hello/<name>')
def hello_name(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))
"""
    url_for() is used to redirect the execution to any specific function through another 
    function with the help of redirect function
    it has two arguments
    first is the name of function which we want to execute
    second is the variables passed as a argument for use of variables in that function
    we can send as many as variables we want
"""

if __name__=='__main__':
    app.run(debug=True)
    
