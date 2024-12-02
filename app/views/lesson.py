from flask import render_template,session
from app.wrapers import isUser
from app.models import Question
from . import app

@app.route('/lesson/1',methods=["GET"])
@isUser
def lesson1():
    return render_template('lesson/lesson1.html',session=session)

@app.route('/lesson/2',methods=["GET"])
@isUser
def lesson2():
    answers = Question.query.filter_by(user=session["userId"],quiz=1).order_by("question")
    return render_template('lesson/lesson2.html',session=session,answers=list(answers))