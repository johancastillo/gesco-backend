# Dependencies imports
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Instance of Flask class
app = Flask(__name__)

# Conection to Data Base MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jcjohan'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'monitor'

mysql = MySQL(app)

# Settings for sessions
app.secret_key = 'mysecretkey'

# Route root
@app.route('/')
def Home():
    # Consulte to the data base
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM providers')
    data = cursor.fetchall()

    # View
    return render_template('index2.html', providers = data)

# Receive data with the method POST from the route root
@app.route('/add-provider', methods = ['POST'])
def AddProvider():
    if request.method == 'POST':
        rif = request.form['rif'] 
        fullname = request.form['fullname'] 
        contributor = request.form['contributor'] 
        phone = request.form['phone'] 
        email = request.form['email'] 
        
        # Get connection
        cursor = mysql.connection.cursor()

        # Write sentence
        cursor.execute('INSERT INTO providers (rif, fullname, contributor, phone, email) VALUES (%s, %s, %s, %s, %s)', 
        (rif, fullname, contributor, phone, email))

        # Execute 
        mysql.connection.commit()
        
        flash('Proveedor agregado correctamente')
        return redirect(url_for('Home'))

# Edit data
@app.route('/edit/<id>')
def GetProvider(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM providers WHERE id = %s', (id))
    data = cursor.fetchall()
    
    return render_template('edit-provider.html', provider = data[0])

@app.route('/update/<id>', methods = ['POST'])
def UpdateContact(id):
    if request.method == 'POST':
        rif = request.form['rif']
        fullname = request.form['fullname']
        contributor = request.form['contributor']
        phone = request.form['phone']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute(""" 
            UPDATE providers
            SET rif = %s,
                fullname = %s,
                contributor = %s,
                phone = %s,
                email = %s
            WHERE id = %s
        """, (rif, fullname, contributor, phone, email, id))

        mysql.connection.commit()

        flash('Proveedor editado correctamente')

        return redirect(url_for('Home'))

# Delete data
@app.route('/delete/<string:id>')
def deleteContact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM providers WHERE id = {0}'.format(id))
    mysql.connection.commit()

    # Message
    flash('Proveedor eliminado correctamente')

    return redirect(url_for('Home'))

# Run server
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 7000, debug = True)

