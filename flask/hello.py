from flask import Flask, render_template, request, redirect, make_response
from flask.helpers import url_for
from werkzeug.utils import secure_filename
import datetime

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

# upload file
@app.route('/upload', methods=['POST','GET'])
def upload():
    if request.method=='POST':
        f=request.files['profile']
        f.save('E:/'+secure_filename(f.filename))
    return render_template('upload.html')

@app.route('/cookie')
def cookie():
    resp=make_response(render_template('cookie.html'))
    print(request.cookies)
    print(request.cookies.get('key'))
    print(request.cookies.get('name'))
    now=datetime.datetime.now()
    week=''
    if now.isoweekday()==1:
        week='Mon'
    elif now.isoweekday()==2:
        week='Tue'
    elif now.isoweekday()==3:
        week='Wed'
    elif now.isoweekday()==4:
        week='Thur'
    elif now.isoweekday()==5:
        week='Fri'
    elif now.isoweekday()==6:
        week='Sat'
    else:
        week='Sun'
    resp.set_cookie('last_access_time',datetime.datetime.strftime(now,'%Y-%m-%d %H:%m:%S'))
    # resp.set_cookie('expires', week+', '+datetime.datetime.strftime(now, '%d '))
    return resp

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

