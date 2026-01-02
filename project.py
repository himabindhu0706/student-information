from flask import Flask, jsonify, request

app = Flask(__name__)

# -------------------------------
# Student Database (Temporary)
# -------------------------------
students = []

# -------------------------------
# Home Route
# -------------------------------
@app.route("/")
def home():
    return "Student Database Backend Running Successfully"

# -------------------------------
# Add Student (POST)
# -------------------------------
@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.json

    student = {
        "name": data["name"],
        "department": data["department"],
        "year": data["year"],
        "email": data["email"]
    }

    students.append(student)
    return jsonify({"message": "Student added successfully"})

# -------------------------------
# Get All Students (GET)
# -------------------------------
@app.route("/get_students", methods=["GET"])
def get_students():
    return jsonify(students)

# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)