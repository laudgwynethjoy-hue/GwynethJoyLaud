from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "2024-00146",
        "name": "Gwyneth Joy Laud",
        "program": "BSIT",
        "year": 3,
        "section": "B"
    })


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

if __name__ == '__main__':
    app.run(debug=True)


