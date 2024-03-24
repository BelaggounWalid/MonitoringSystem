from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__, template_folder='template')

def connect_db():
    return sqlite3.connect('/home/anis/Secondstep/anisdatabase.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    try:
        # Get the database connection
        db = get_db()

        # Fetch the first row from the cert_alert table
        cursor = db.execute('SELECT * FROM cert_alert ORDER BY rowid DESC LIMIT 1')
        cert_data = cursor.fetchone()

        # Fetch data from the dataBase table
        cursor = db.execute('SELECT * FROM dataBase')
        elements = cursor.fetchall()

        return render_template('page.html', elements=elements, cert_data=cert_data)
    except Exception as e:
        return f"An error occurred: {str(e)}"
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

