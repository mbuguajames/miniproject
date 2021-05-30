import mysql.connector as database  # MYSQL driver to access the MYSQL database
from flask import Flask, render_template, request

app = Flask(__name__)

connection = database.connect(
    user="root",  # app.config['MYSQL_USER']
    password="",  # app.config['MYSQL_PASSWORD']
    host="localhost",  # app.config['MYSQL_HOST']
    database="webappproject")  # app.config['MYSQL_DATABASE']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        contact_email = request.form['email']
        contact_first_name = request.form['firstname']
        contact_lastname = request.form['lastname']
        contact_message = request.form['message']
        cursor = connection.cursor()
        """
        relook
        """
        contact_sql = "INSERT INTO userdetails (email, firstname, lastname, message) VALUES(%s,%s,%s,%s)"  # Incorrect
        contact_val = (contact_email, contact_first_name, contact_lastname, contact_message)  # This was missing
        cursor.execute(contact_sql, contact_val)
        connection.commit()
        cursor.close()
        return f"Done!!"
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()
