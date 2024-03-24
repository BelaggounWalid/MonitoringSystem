from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    try:
        # Get the database connection
        db = get_db()

        # Fetch the first row from the cert_alert table
        cursor = db.execute('SELECT * FROM cert_alert ORDER BY rowid DESC LIMIT 1')
        cert_data = cursor.fetchone()

        # Fetch data from the dataBase table
        cursor = db.execute('SELECT * FROM dataBase')
        elements = cursor.fetchall()

        # Render the template with the fetched data
        return render_template('page.html', elements=elements, cert_data=cert_data)
    except Exception as e:
        return f"An error occurred: {str(e)}"
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

@app.route('/update_seuil', methods=['GET', 'POST'])
def update_seuil():
    if request.method == 'GET':
        try:
            # Get the database connection
            db = get_db()

            # Fetch the first row from the Seuil table
            cursor = db.execute('SELECT * FROM Seuil ORDER BY rowid LIMIT 1')
            cert_data = cursor.fetchone()

            return render_template('form.html', cert_data=cert_data)
        except Exception as e:
            return f"An error occurred: {str(e)}"
    elif request.method == 'POST':
        try:
            # Get the form data
            cpu = request.form['cpu']
            memory = request.form['memory']
            ram = request.form['ram']
            temps_limite = request.form['temps_limite']

            # Update the first row of the Seuil table
            db = get_db()
            db.execute('UPDATE Seuil SET cpu = ?, memory = ?, ram = ?, temps_limite = ? WHERE rowid = 1', (cpu, memory, ram, temps_limite))
            db.commit()

            # Redirect to the home page
            return redirect(url_for("index"))
        except Exception as e:
            return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

