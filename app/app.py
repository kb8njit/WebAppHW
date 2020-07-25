from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'OscarData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Kelly'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM OscarWinners')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, oscars=result)


@app.route('/view/<int:oscar_id>', methods=['GET'])
def record_view(oscar_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM OscarWinners WHERE id=%s', oscar_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', oscar=result[0])


@app.route('/edit/<int:oscar_id>', methods=['GET'])
def form_edit_get(oscar_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM OscarWinners WHERE id=%s', oscar_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', oscar=result[0])


@app.route('/edit/<int:oscar_id>', methods=['POST'])
def form_update_post(oscar_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Year'), request.form.get('Movie_Title'), request.form.get('Name'), request.form.get('Age'), request.form.get('Gender'), oscar_id)
    sql_update_query = """UPDATE OscarWinners t SET t.Year = %s, t.Movie_Title = %s, t.Name = %s, t.Age = %s, t.Gender = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/oscar/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Oscar Winner Entry')


@app.route('/oscar/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Year'),request.form.get('Name'), request.form.get('Age'), request.form.get('Gender'),)
    sql_insert_query = """INSERT INTO OscarWinners (Year, Name,Age,Gender) VALUES (%s,%s,%s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/delete/<int:oscar_id>', methods=['POST'])
def form_delete_post(oscar_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM OscarWinners WHERE id = %s """
    cursor.execute(sql_delete_query, oscar_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/oscars', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM OscarWinners')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/oscars/<int:osar_id>', methods=['GET'])
def api_retrieve(oscar_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM OscarWinners WHERE id=%s', oscar_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/oscars/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/oscars/<int:oscar_id>', methods=['PUT'])
def api_edit(oscar_id) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/oscars/<int:oscar_id>', methods=['DELETE'])
def api_delete(oscar_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)