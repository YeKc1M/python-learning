from flask import Flask, render_template
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

