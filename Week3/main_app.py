from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from pymysql import cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'school'

mysql = MySQL(app)
mysql = MySQL(cursorclass=cursors.DictCursor)
mysql.init_app(app)


@app.route("/", methods=['GET', "POST"])
def index():
    if request.method == 'POST':
        details = request.form
        id = details['ID']
        name = details['Name']
        subject = details['Subject']
        salary = details['Salary']
        cur1 = mysql.connect().cursor()
        cur1.execute(
            "INSERT INTO teachers (id, name, subject, salary) VALUES (%d, %s, %s, %d)")
        mysql.connect().commit()
        return "SUCCESS!"
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
