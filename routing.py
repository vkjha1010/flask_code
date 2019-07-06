"""
    program to understand the routing technique in flask
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')               # if we write http://localhost:5000/ on browser then welcome function will call
def welcome():
    return "Welcome In The Routing Technique"

@app.route('/hello')          # if we write http://localhost:5000/hello on browser then hello_tutorial() function will call
def hello_tutorial():
    return "Hello, This is the routing technque tutorial"

if __name__=='__main__':
    app.run(debug=True)
