from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create Database
def create_database():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()

create_database()

# Home Page
@app.route('/')
def home():
    return get_students()
# Add Student
@app.route('/add_student', methods=['POST'])
def add_student():

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student(name,email,course) VALUES(?,?,?)",
        (
            data['name'],
            data['email'],
            data['course']
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student Added Successfully"})

# View Students
@app.route('/students', methods=['GET'])
def get_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")

    students = cursor.fetchall()

    conn.close()

    return jsonify(students)

# Delete Student
@app.route('/delete_student/<int:id>', methods=['DELETE'])
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM student WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student Deleted Successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)