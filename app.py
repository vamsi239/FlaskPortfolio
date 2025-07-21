from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Add this for flashing messages


# ------------------- DATABASE INITIALIZATION ------------------- #
def init_db():
    conn = sqlite3.connect('contact.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            project TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ------------------- HOME ROUTE ------------------- #
@app.route('/')
def index():
    certificates = [
        {
            "title": "Mastering DSA using C and C++",
            "image": "certificates/DSA.png",
            "pdf": "certificates/Mastering DSA using C and C++.pdf"
        },
        {
            "title": "HTML, CSS, Javascript for Web Developers",
            "image": "certificates/HTML1.png",
            "pdf": "certificates/HTML, CSS, Javascript for Web Developers.pdf"
        },
        {
            "title": "ServerSide Javascript With Node.JS",
            "image": "certificates/Node1.png",
            "pdf": "certificates/ServerSide Javascript.pdf"
        },
    ]

    internships = [
        {
            "title": "Cipher Schools",
            "subtitle": "DataStructures & Algorithms",
            "image": "certificates/CIPHER.png",
            "certificate_pdf": "certificates/Cipherschools.pdf",
            "description": [
                "Proficient in time and space complexity analysis using Big O notation",
                "Strong understanding of recursion and iterative problem-solving techniques",
                "Developed projects using non-linear data structures",
                "Applied DSA principles to optimize code performance and reduce runtime/memory usage."
            ]
        },
        {
            "title": "DBASE Solutions",
            "subtitle": "Database Management Specialist",
            "image": "certificates/DB.png",
            "certificate_pdf": "certificates/DB SOLUSIONS.pdf",
            "description": [
                "Managed and optimized database systems to ensure high performance and data integrity",
                "Designed and implemented robust database architectures and schemas",
                "Developed and maintained complex SQL queries, stored procedures, and scripts",
                "Collaborated with cross-functional teams to ensure seamless integration with other systems."
                
            ]
        }
    ]
    
    projects = [
        {
            "title": "Royal Recipe",
            "subtitle": "Front-End",
            "image": "certificates/therecipecritic-homepage.webp",
            "description": [
                "Developed a user-friendly restaurant ordering platform using React for frontend",
                "Managed state with React Hooks to boost performance and scalability",
                "Designed real-time inventory updates and order tracking for enhanced UX",
                "Optimized for responsiveness across various devices"
            ]
        },
        {
            "title": "Music Streaming App",
            "subtitle": "Node.js & Express",
            "image": "certificates/music.jpeg",
            "description": [
                "Developed music streaming platform with Node.js ensuring seamless audio playback and user interaction",
                "Streamlined music playback with playlist support.",
                "Built using REST APIs and integrated MongoDB backend.",
                "Supports user accounts and favorite songs."
            ]
        }
    ]
    
    return render_template("index.html", certificates=certificates, internships=internships, projects=projects)

# ------------------- CONTACT FORM ROUTES ------------------- #

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    project = request.form['project']
    message = request.form['message']

    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, project, message) VALUES (?, ?, ?, ?)",
              (name, email, project, message))
    conn.commit()
    conn.close()

    flash("Your message has been submitted successfully!", "success")
    return redirect(url_for('index'))

# ------------------- MAIN ------------------- #
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
