from flask import Flask, render_template, make_response, request
from flask.helpers import url_for
import requests
import sapcai

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# https://api.cai.tools.sap/build/v1/dialog ?
# REQUEST_TOKEN d475521f36a9539e5e4d673bf807c3f4
# USER_SLUG yekc1m
@app.route('/cai', methods=['POST', 'GET'])
def cai():
    answer=None
    if request.method=='POST':
        question=request.form.get('question')
        answer=question
        build=sapcai.Build("d475521f36a9539e5e4d673bf807c3f4", 'en')
        response=build.dialog({'type':'text', 'content':question},'CONVERSATIONAL_ID')
        # print(response.messages[0].content)
        return render_template('cai.html', answer=response.messages[0].content)
    return render_template('cai.html')

if __name__=='__main__':
    app.run(debug=True)