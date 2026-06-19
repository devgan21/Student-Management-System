from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Student Management Dashboard</title>
    </head>

    <body>
        <h1>Student Management System</h1>

        <h2>CDAC Mini Project</h2>

        <h3>Technologies Used</h3>

        <ul>
            <li>Tkinter GUI</li>
            <li>Flask REST API</li>
            <li>SQLite Database</li>
            <li>Django Dashboard</li>
        </ul>

        <h3>Features</h3>

        <ul>
            <li>Add Student</li>
            <li>View Students</li>
            <li>Delete Student</li>
            <li>Database Storage</li>
        </ul>

    </body>
    </html>
    """)