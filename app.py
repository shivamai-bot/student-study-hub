
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary task storage
tasks = []
next_task_id = 1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/planner", methods=["GET", "POST"])
def planner():
    global next_task_id

    if request.method == "POST":
        task_name = request.form.get("task", "").strip()

        if task_name:
            tasks.append({
                "id": next_task_id,
                "name": task_name,
                "completed": False
            })
            next_task_id += 1

        return redirect(url_for("planner"))

    return render_template("planner.html", tasks=tasks)


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

    return redirect(url_for("planner"))



@app.route("/resources")
def resources():
    study_resources = [
        {
            "title": "Python Programming",
            "description": "Learn Python fundamentals, syntax, and examples.",
            "url": "https://docs.python.org/3/tutorial/"
        },
        {
            "title": "HTML and CSS",
            "description": "Learn how to structure and style web pages.",
            "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development"
        },
        {
            "title": "Flask Web Development",
            "description": "Understand routes, templates, and web applications.",
            "url": "https://flask.palletsprojects.com/en/stable/tutorial/"
        },
        {
            "title": "Git and GitHub",
            "description": "Learn version control and how to manage project code.",
            "url": "https://docs.github.com/en/get-started"
        }
    ]

    return render_template(
        "resources.html",
        study_resources=study_resources
    )




@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False
    error_message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            error_message = "Please fill in all fields."
        elif "@" not in email or "." not in email.split("@")[-1]:
            error_message = "Please enter a valid email address."
        else:
            message_sent = True

    return render_template(
        "contact.html",
        message_sent=message_sent,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)
