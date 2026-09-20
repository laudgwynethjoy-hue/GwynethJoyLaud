from flask import Flask, jsonify, request

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to my first API!"

# Student Route
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "2026-00146",
        "name": "Gwyneth Joy Laud",
        "program": "BSIT",
        "year": 3,
        "section": "B"
    })

# Hello Route
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })

# Skills Endpoint
@app.route('/skills')
def get_skills():
    return jsonify({
        "student": "Gwyneth Joy Laud",
        "skills": [
            "Python",
            "Flask",
            "HTML",
            "CSS",
            "JavaScript",
            "MySQL"
        ]
    })

# Run the App
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
