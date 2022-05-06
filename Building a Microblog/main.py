# Kyle Orcutt

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, request, redirect
from datetime import datetime
import os, json
from google.cloud import datastore


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

dataClient = datastore.Client()

@app.route('/')
def newpage():
    return 'Welcome to Lab 3!'

@app.route('/editor')
def edit_page():
    with open('editor.html', 'r') as page:
        return page.read()

@app.route('/submit', methods = ['POST'])
def submit_post():
    password = request.form['pass']
    if password == "mySuperAwesomePassword":
        content = request.form['content']
        title = request.form['title']
        time = str(datetime.utcnow())


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
