from flask import Flask, render_template, redirect, request
from flask_login.utils import login_user, logout_user
from google_auth_oauthlib.flow import Flow
import os
import requests
import google.auth.transport.requests
from google.oauth2 import id_token
from flask_login import LoginManager, current_user
import json

from user import User
from db_handler import db

app = Flask(__name__)
app.debug = True

login_manager = LoginManager()
app.secret_key = b'\xce\xf1z\xdd\x11^\xa8\xaf\xf02\xbb\xb8\xf7\x97\x99\xdd{\xffr\xd5}\xabP\x9e'
# Why is security such a nightmare to deal with 
login_manager.init_app(app)

database = db()

#CHANGE THIS ON RELEASE
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'

CLIENT_ID = None

with open("client_secrets.json") as file:
    data = json.loads(file.read())
    CLIENT_ID = data['web']['client_id'] 


flow = Flow.from_client_secrets_file(
    client_secrets_file='client_secrets.json',
    scopes=["https://www.googleapis.com/auth/userinfo.profile", 
    "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:5000/signin/callback"
    )

@login_manager.user_loader
def loadUser(userid):
    return User.get(userid, database)


@app.route("/", methods=['GET', "POST"])
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/compete", methods=['GET'])
def compete():
    return render_template('compete.html')

@app.route("/leaderboard")
def leaderboard():
    return render_template('leaderboard.html')

@app.route("/practice")
def practice():
    return render_template('practice.html')

@app.route("/signin", methods=["GET", "POST"])
def signin():
    authorization_url, state = flow.authorization_url()
    return redirect(authorization_url)

@app.route("/trending")
def trending():
    return render_template('trending.html')

@app.route("/dashboard", methods=['GET'])
def dashboard():
    if current_user.is_authenticated:
        return render_template("dashboard.html")

    return "Fuck off"

@app.route("/signin/callback", methods=["GET"])
def callback():
    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials
    requestSession = requests.session()
    token_request = google.auth.transport.requests.Request(session=requestSession)

    idToken = id_token.verify_oauth2_token(
        id_token=credentials.id_token,
        request=token_request,
        audience=CLIENT_ID
    )
    
    user = User(idToken["sub"], idToken["name"], idToken["email"])
    if not User.get(user.id, database):
        user.create(user.id, user._name, user._email, database)
    login_user(user)    

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.run()