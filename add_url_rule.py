"""
    program to use the add_url_rule()
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome In The Routing Technique"

@app.route('/hello')
def hello_tutorial():
    return "Hello, This is the routing technque tutorial"

def home():
    return "My Home Page"
app.add_url_rule('/home','home',home)     
"""
    we can use add_url_rule() for the same purpose as route() is used, but we can use add_url_rule() to create dynamic url
    it has three arguments 
      first one is url
      second is end point (which is generally same as the name of function associated)
      third is the function name which is associated with that add_url_rule()
"""

if __name__=='__main__':
    app.run(debug=True)
