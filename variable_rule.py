"""
    program to create dynamic url with different data types
"""

from flask import Flask
app=Flask(__name__)

"""
    if we will write localhost:5000/hello/Vikas it will show as Hello Vikas 
    Vikas will be stored in name variable and that name is passed in function as a argumment
"""
@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s'%name

"""
    if we want to take an integer value as an argument, we use int: before variable name
    by default data type will be string, as we seen above
"""
@app.route('/blog/<int:postID>')
def blog_no(postID):
    return 'Blog Number is %d' %postID

# if we want to take a float value as an argument, we use float: before variable name
@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number is %f' % revNo

if __name__=='__main__':
    app.run(debug=True)
    
