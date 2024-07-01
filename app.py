from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="elvo",
    password="Elvo=1234",
    database="user_db"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    full_name = request.form['full-name']
    email = request.form['email']
    source = request.form['source']
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (full_name, email, source) VALUES (%s, %s, %s)", (full_name, email, source))
    db.commit()
    
    return redirect(url_for('index'))

@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    full_name = request.form['full-name']
    email = request.form['email']
    source = request.form['source']
    
    cursor = db.cursor()
    cursor.execute("UPDATE users SET full_name=%s, email=%s, source=%s WHERE id=%s", (full_name, email, source, id))
    db.commit()
    
    return redirect(url_for('index'))

# methods=['POST']
@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
