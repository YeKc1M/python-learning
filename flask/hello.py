from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
app=Flask(__name__)

@app.route('/')
def index():
    return '''<head>
        <title>index</title>
    </head>
    <body>
        <h1>this is index</h1>
    </body>'''

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error=None
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if(username=='mky' and password=='123'):
            return render_template('hello.html', name=username)
        else:
            error='Invalid username and password POST'
    elif request.method=='GET':
        username=request.args.get('username')
        password=request.args.get('password')
        if(username=='mky' and password=='123'):
            return render_template('hello.html', name=username)
        else:
            error='Invalid username and password GET'
    return render_template('login.html', error=error)

# url_for(func_name, args)
@app.route('/try_url/')
def try_url():
    return '''url_for'''

if __name__=='__main__':
    app.run(debug=True)
    # test url_for
    # with app.test_request_context():
    #     print(url_for('try_url'))
    #     print(url_for('try_url',arg1='arg1',arg2='arg2'))

