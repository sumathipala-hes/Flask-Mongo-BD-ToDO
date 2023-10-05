from flask.templating import render_template_string
from werkzeug.datastructures import RequestCacheControl
from application import app, db
from flask import render_template, flash, redirect, request
from .forms import TodoForm
from datetime import datetime


@app.route("/")
def index():
    return render_template("view_todos.html", title = "Todos")

@app.route("/add_todo", methods = ['POST', 'GET'])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        competed = form.completed.data
        
        db.todo.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": competed,
            "date_completed":datetime.utcnow()      
        })
        flash("ToDo successfully added", "success")
        return redirect("/")
    else:  
        form = TodoForm()
    return render_template("add_todo.html", form = form)