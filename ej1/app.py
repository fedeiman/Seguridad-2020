#!/usr/bin/env python
#
# Welcome to Gringotts!

import hashlib
import json
import logging
import os
import sqlite3
import subprocess
import sys

from flask import (Flask, request, session, g, redirect, url_for,
                    render_template, flash)
from werkzeug import debug


app = Flask(__name__)


# Generate test data when running locally
data_dir = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(data_dir):
    import generate_data
    os.mkdir(data_dir)
    generate_data.main(data_dir, 'dummy-password', 'dummy-proof', 'dummy-plans')

secrets = json.load(open(os.path.join(data_dir, 'secrets.json')))

# Turn on backtraces, but turn off code execution (that'd be an easy level!)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.wsgi_app = debug.DebuggedApplication(app.wsgi_app, evalex=False)

app.logger.addHandler(logging.StreamHandler(sys.stderr))
# use persistent entropy file for secret_key
app.secret_key = open(os.path.join(data_dir, 'entropy.dat')).read()


@app.route('/')
def index():
    """Main page."""
    try:
        user_id = session['user_id']
    except KeyError:
        secret = None
    else:
        secret = secrets[str(user_id)]
    return render_template('index.html', secret=secret)


@app.route('/logout')
def logout():
    """Logout user."""
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/login', methods=['POST'])
def login():
    """Validate user and display secret."""
    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
        flash("Se debe ingresar un usuario")
        return redirect(url_for('index'))

    if not password:
        flash("Se debe ingresar el password")
        return redirect(url_for('index'))

    conn = sqlite3.connect(os.path.join(data_dir, 'users.db'))
    cursor = conn.cursor()

    query = """SELECT id, password_hash, salt FROM users
                WHERE username = '%s' LIMIT 1""" % username
    cursor.execute(query)
    res = cursor.fetchone()

    if not res:
        flash("No existe el usuario %s!" % username)
        return redirect(url_for('index'))

    user_id, password_hash, salt = res
    calculated_hash = hashlib.sha256( salt + password + salt)  # <-.->
    if calculated_hash.hexdigest() != password_hash:
        flash("Password incorrecta para %s!" % username)
        return redirect(url_for('index'))

    session['user_id'] = user_id
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
