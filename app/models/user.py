from app import db
from sqlalchemy import Column, Integer, String,Enum,ForeignKey

class User(db.Model):
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True, nullable=False)
	password = Column(String(128), nullable=False)
	kind = Column(Enum('user','mod','admin',name="user_kind"),nullable=False)

	def isAdmin(id):
		user = User.query.filter_by(id=id).first()
		if user and user.kind == 'admin':
			return True
		else:
			return False

	def isMod(id):
		user = User.query.filter_by(id=id).first()
		if user and user.kind == 'mod':
			return True
		else:
			return False
	
	def isUser(id):
		user = User.query.filter_by(id=id).first()
		if user:
			return True
		else:
			return False


class Question(db.Model):
	id = Column(Integer, primary_key=True)
	user =  Column(Integer, ForeignKey('user.id'), nullable=False)
	quiz = Column(Integer, nullable=False)
	question = Column(Integer, nullable=False)
	answer = Column(Integer, nullable=False)