from flask import Flask, render_template
from flask_mysqldb import MySQL

from flask_wtf import Form
from wtforms import StringField

class NewStudentForm(Form):
    name = StringField('Student Name')
    email = StringField('Email')

mysql = MySQL()
app = Flask(__name__)

# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '10021996'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '146.148.67.222'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello():
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add")
def add():
    form = NewStudentForm()
    return render_template('add.html', form=form)
    #cur = mysql.connection.cursor()
    #cur.execute('''INSET INTO students (studentName, email) VALUES ('Michael Jones', 'm.jones@mydit.ie')''')


if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000
