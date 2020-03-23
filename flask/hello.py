from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '''<head>
        <title>index</title>
    </head>
    <body>
        <h1>this is index</h1>
    </body>'''

if __name__=='__main__':
    app.run()