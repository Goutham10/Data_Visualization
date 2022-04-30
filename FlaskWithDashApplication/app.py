import os
from flask import Flask, render_template, request,redirect, url_for
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import psycopg2
import werkzeug
from dash_application.dash_functionalities import  create_dash_application, create_excel_dash,file_fetching
from werkzeug.utils import secure_filename

data_to_dash = ''

app = Flask(__name__)
create_dash_application(app)
create_excel_dash(app)




DB_HOST = 'localhost'
DB_NAME = 'postgre_flask'
DB_USER = 'postgres'
DB_PASS = 'sunny123'

connection_object = psycopg2.connect(host = DB_HOST,
                    database = DB_NAME,
                    user = DB_USER,
                    password = DB_PASS)
cursor = connection_object.cursor()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/home_page/<user>')
def home_page(user):
    return render_template('home_page.html', user = user)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/file_based')
def file_based():
    return render_template('result.html')

@app.route('/register_person', methods = ['POST', 'GET'])
def saving_details():
    print("entered method.....")
    if request.method == 'POST':
        try:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            user_name = request.form.get('user_name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            cursor.execute(""" INSERT INTO register_person_table (first_name, last_name, user_name, email, password, confirm_password) 
                               VALUES(%s,%s,%s,%s,%s,%s)
                           """, (first_name, last_name, user_name, email, password,confirm_password))
            connection_object.commit()
            print("data inserted")
        except:
            print("invalid")
        finally:
            return redirect(url_for('login'))
    else:
        try:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            user_name = request.form.get('user_name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            # print(first_name, last_name, user_name, email, password, repeated_password)
            cursor.execute(""" INSERT INTO register_person_table (first_name, last_name, user_name, email, password, confirm_password) 
                               VALUES(%s,%s,%s,%s,%s,%s)
                           """, (first_name, last_name, user_name, email, password,confirm_password))
            connection_object.commit()
            print("data inserted")
        except:
            print("invalid")
        finally:
            return redirect(url_for('index'))


@app.route('/validate_login', methods = ['POST', 'GET'])
def validate():
    print("enter for validation")
    if request.method == 'POST':
        try:
            user_name = request.form.get('user_name')
            password = request.form.get('password')
            print(user_name, password)
            
            cursor.execute(" select user_name, password from register_person_table where user_name = %s",(user_name,))
            data = cursor.fetchone()
            db_user_name = data[0]
            db_password = data[1]
            
            if ((user_name == db_user_name) and (password == db_password)):
                print("valid data")
                return redirect(url_for("home_page", user = data[0]))
            else:
                print("invalid data")
                return redirect(url_for('login'))
                        
        except Exception as e:
            print("invalid  details", e)
        
@app.route('/file_based_data')
def file_based_data():
    return render_template("filebased.html")

@app.route('/file_input', methods = ['POST', 'GET'])
def file_input():
    if request.method == 'POST':
        try:
            if request.method == 'POST':
                f = request.files['file']
                f.save(secure_filename(f.filename))
                fn = os.path.basename(f.filename)
                print(type(fn))
                global df
                df = pd.read_excel('{0}'.format(fn))
                print(type(df))
                file_fetching(df)
                
                return redirect(url_for('file_based'))
        except:
             print("invalid")
        finally:
            data_to_dash = df
            print("data_to_dash")
            print(data_to_dash)
            return redirect(url_for('file_based'))


if __name__ == "__main__":
    app.run(debug=True)