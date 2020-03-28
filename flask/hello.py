from flask import Flask, render_template, request, redirect, make_response, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import secure_filename
import datetime

app=Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

def getGMTTime(time):
    week=''
    if time.isoweekday()==1:
        week='Mon'
    elif time.isoweekday()==2:
        week='Tue'
    elif time.isoweekday()==3:
        week='Wed'
    elif time.isoweekday()==4:
        week='Thur'
    elif time.isoweekday()==5:
        week='Fri'
    elif time.isoweekday()==6:
        week='Sat'
    else:
        week='Sun'
    month=''
    m=time.month
    if m==1:
        month='Jan'
    elif m==2:
        month='Feb'
    elif m==3:
        month='Mar'
    elif m==4:
        month='Apr'
    elif m==5:
        month='May'
    elif m==6:
        month='Jun'
    elif m==7:
        month='Jul'
    elif m==8:
        month='Aug'
    elif m==9:
        month='Sep'
    elif m==10:
        month='Oct'
    elif m==11:
        month='Nov'
    else:
        month='Dec'
    # resp.set_cookie('expires', week+', '+datetime.datetime.strftime(now, '%d '))expires=Mon, 23 Mar 2020 1:00:00 UTC
    return week+', '+str(time.day)+" "+month+datetime.datetime.strftime(time, " %Y %H:%m:%S UTC")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error=None
    if request.method=='POST':
        # if request.cookies.get('username')=='mky' and request.cookies.get('password')=='123':
        #     return redirect(url_for('index'))
        username=request.form['username']
        password=request.form['password']
        if(username=='mky' and password=='123'):
            #return render_template('hello.html', name=username)
            auto_log=request.form.get('auto_login')
            if auto_log:
                resp=make_response(render_template('index.html'))
                resp.set_cookie('username', username)
                resp.set_cookie('password', password)
                resp.set_cookie('expires', getGMTTime(datetime.datetime.now()))
                return resp
            flash("successful login")
            flash("flash 2")
            return redirect(url_for('index'))
        else:
            error='Invalid login'
    elif request.method=='GET':
        if request.cookies.get('username')=='mky' and request.cookies.get('password')=='123':
            return redirect(url_for('index'))
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

# ajax learning
@app.route('/ajax')
def ajax():
    return render_template('ajax.html')

@app.route('/add_numbers')
def add_numbers():
    a=request.args.get('a', 0, type=int)
    b=request.args.get('b', 0, type=int)
    return jsonify(result=a+b)
    # return jsonify({'name':'mky','sid':'213171900'})
@app.route('/ajax_text')
def ajax_text():
    text=request.args.get('text', type=str)+' back'
    return jsonify(result=text)

if __name__=='__main__':
    app.run(debug=True)
    # test url_for
    # with app.test_request_context():
    #     print(url_for('try_url'))
    #     print(url_for('try_url',arg1='arg1',arg2='arg2'))

