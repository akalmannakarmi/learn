from flask import render_template,session,request,redirect
from app.wrapers import isUser
from . import app

@app.route('/lesson/1',methods=["GET"])
@isUser
def lesson1():
    return render_template('lesson/lesson1.html',session=session)