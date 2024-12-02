from flask import session,request,redirect,jsonify
from . import app
from app import db
from app.models import Question
from app.wrapers import isUser

@app.route('/lesson/2',methods=["POST"])
@isUser
def lesson2():
	data = request.form
	rq=['q1','q2','q3','q4']
	if any(i not in data for i in rq):
		result = {"Require":{','.join(rq)}}
		return jsonify(str(result))

	for i,q in enumerate(rq):
		question = Question(user=session["userId"],quiz=1,question=i+1,answer=data[q])
		db.session.add(question)
	db.session.commit()

	return redirect('/lesson/2')