from flask import Flask, render_template, request, redirect
import json
import os
from datetime import date

app = Flask(__name__)
DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

@app.route("/")
def home():
    tasks = load_tasks()
    today = date.today().isoformat()
    for t in tasks:
        t["overdue"] = (not t["done"]) and t["due_date"] and t["due_date"] < today
    tasks.sort(key=lambda t: t["due_date"] or "9999-99-99")
    return render_template("index.html", tasks=tasks, today=today)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        tasks = load_tasks()
        new_task = {
            "id": (max([t["id"] for t in tasks], default=0)) + 1,
            "title": request.form["title"],
            "priority": request.form["priority"],
            "category": request.form["category"],
            "due_date": request.form["due_date"],
            "done": False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if request.method == "POST":
        task["title"] = request.form["title"]
        task["priority"] = request.form["priority"]
        task["category"] = request.form["category"]
        task["due_date"] = request.form["due_date"]
        save_tasks(tasks)
        return redirect("/")
    return render_template("edit.html", task=task)

@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
