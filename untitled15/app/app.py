from typing import List, Dict
import simplejson as json
from flask import Flask
from flask import render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import re

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'LoginData'
mysql.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)