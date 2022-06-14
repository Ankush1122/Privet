from crypt import methods
import MainRepo
from flask import Flask, render_template, redirect, session, send_file, request
from flask_mail import Mail, Message
from flask.helpers import url_for

import os

app = Flask(__name__)


if(os.environ.get('ENV') == "Production"):
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

mail = Mail(app)
db = MainRepo.Repo(app.config)

from User.UserController import user

app.register_blueprint(user, url_prefix="/user")


@app.route('/home', methods=['GET'])
def home():
    if (not session.get("index") is None):
        return redirect(url_for('user.profile'))
    return redirect(url_for('user.login'))


@app.route('/logo', methods=['GET'])
def logo():
    return send_file('static/assets/img/hero-img.png')


@app.route('/', methods=['GET'])
@app.route('/Home', methods=['GET'])
def redir():
    return redirect(url_for('home'))


@app.before_request
def beforeRequest():

    if(app.config["ENV"] == "production"):
        if not request.url.startswith('https'):
            return redirect(request.url.replace('http', 'https', 1))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
