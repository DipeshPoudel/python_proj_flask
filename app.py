from flask import Flask, render_template
from db_connect import get_connection

app = Flask(__name__)
subjects = ['Python','Database','Data Science','Java']

@app.route("/")
def index():
    return render_template('index.html',name='Jack', subjects=subjects)

@app.route("/about")
def about():
    return 'I am Dipesh. Welcome to my Class'

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/students")
def students():
    with get_connection().cursor() as cur:
        cur.execute("SELECT * FROM student")
        students = cur.fetchall()
    return render_template('student.html',students=students)

if __name__ == '__main__':
    app.run(debug=True)