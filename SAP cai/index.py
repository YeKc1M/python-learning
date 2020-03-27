from flask import Flask, render_template, make_response, request
from flask.helpers import url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# https://api.cai.tools.sap/build/v1/dialog ?
@app.route('/cai', methods=['POST', 'GET'])
def cai():
    answer=None
    if request.method=='POST':
        question=request.form.get('question')
        answer=question
        return render_template('cai.html', answer=answer)
    return render_template('cai.html')

if __name__=='__main__':
    app.run(debug=True)