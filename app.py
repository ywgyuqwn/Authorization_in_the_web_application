import requests
from flask import Flask, render_template, request
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(database="service__db",
                        user="postgres",
                        password="coconimo00F",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    error = ''
    username = request.form.get('username')
    password = request.form.get('password')
    if str(username)=='' and str(password)=='':
        error = 'Нет данных'
        return render_template('account.html',error=error)
    elif str(username)=='':
        error = 'Ошибка..'
        return render_template('account.html',error=error)
    if str(password)=='':
        error = 'Ошибка'
        return render_template('account.html',error=error)
    else:
        cursor.execute("SELECT * FROM service__db.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        if not records:
            error = 'Неправильный логин или пароль'
            return render_template('account.html',error=error)
        else:
            return render_template('account.html', full_name=records[0][1], login=records[0][2],password=records[0][3], error=error)

if __name__ == '__main__':
    app.run()


