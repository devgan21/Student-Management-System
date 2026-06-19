import tkinter as tk
from tkinter import messagebox
import requests

# Add Student
def add_student():

    data = {
        "name": name_entry.get(),
        "email": email_entry.get(),
        "course": course_entry.get()
    }

    response = requests.post(
        "http://127.0.0.1:5000/add_student",
        json=data
    )

    messagebox.showinfo(
        "Success",
        response.json()["message"]
    )

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


# View Students
def view_students():

    response = requests.get(
        "http://127.0.0.1:5000/students"
    )

    students = response.json()

    result.delete(1.0, tk.END)

    for student in students:

        result.insert(
            tk.END,
            f"ID: {student[0]} | Name: {student[1]} | Email: {student[2]} | Course: {student[3]}\n"
        )


# Main Window
root = tk.Tk()

root.title("Student Management System")
root.geometry("700x500")

# Name
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Email
tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Course
tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root, width=40)
course_entry.pack()

# Buttons
tk.Button(
    root,
    text="Add Student",
    command=add_student
).pack(pady=10)

tk.Button(
    root,
    text="View Students",
    command=view_students
).pack(pady=10)

# Result Box
result = tk.Text(root, height=15, width=80)
result.pack()

root.mainloop()