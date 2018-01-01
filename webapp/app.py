from flask import Flask, render_template, redirect, url_for, request

from student import Student2
students = []

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])  # function decorator
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id","")  # dictionaries @ html
        new_student_name = request.form.get("name","")
        new_student_last_name = request.form.get("last-name","")

        new_student = Student2(name=new_student_name, last_name=new_student_last_name, student_id=new_student_id)
        students.append(new_student)

        return redirect(url_for("students_page"))  # back to the same page they came from - good practice
    return render_template("index.html",students=students)  # students to be use inside the html


if __name__ == '__main__':
    app.run(debug=True)

# pip3 / pip install flask in terminal (all open a flask project in PyCharm, auto installed to Python packages..)