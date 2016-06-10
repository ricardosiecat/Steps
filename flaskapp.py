import os
from datetime import datetime
from flask import Flask, g, render_template, flash, redirect, url_for, jsonify, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_qrcode import QRcode

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return 'Hey'

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run()
