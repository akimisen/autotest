from datetime import datetime
# import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, url_for
from flask_login import UserMixin
#from app.exceptions import ValidationError
from . import db, login_manager

class User(UserMixin,db.Model):
  __tablename__ = 'user'
  user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_name = db.Column(db.String(20), unique=True)
  pwd_hash = db.Column(db.String(128))
  group_id = db.Column(db.Integer, db.ForeignKey('department.department_id'))
  # cases_owned_by_user = db.relationship('CaseInfo', backref='User', lazy='dynamic')

  def __repr__(self):
      return '<User %r>' % self.user_name

  @property
  def id(self):
    return self.user_id
  
  @id.setter
  def id(self):
    self.id=self.user_id

  @property
  def password(self):
    raise AttributeError('password is not readable.')

  @password.setter
  def password(self, password):
    self.pwd_hash = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.pwd_hash,password)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class CaseInfo(db.Model):
  __tablename__='case_info'
  case_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  case_name = db.Column(db.String(50))
  user_id = db.Column(db.Integer, nullable=False)
  group_id = db.Column(db.Integer, nullable=False)
  project_id = db.Column(db.Integer, nullable=False)
  updated_time = db.Column(db.DateTime)
  case_description = db.Column(db.Text(100))
  case_model = db.Column(db.Enum('http','web_ui','app_ui'))

  __mapper_args__ = {
    "order_by": updated_time.desc()
  }
  # @property
  # def info(self):
  #   return self.info

  # @info.setter
  # def info(self):
  #   self.info = dict(case_id=case_id,user_id=user_id,group_id=group_id,project_id=project_id,case_description=case_description)

# class Case(db.Model):
#   @staticmethod
#   def exists_case(case_name):
#     return Case.query.filter_by(case_name=case_name).first()

class RestCase(db.Model):
  __tablename__='rest_case'
  case_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
  url=db.Column(db.String(100), nullable=False)
  method=db.Column(db.Enum('GET','POST','OPTION','DELETE'), server_default='GET')
  # auth=db.Column(db.Boolean)
  data=db.Column(db.JSON)
  headers=db.Column(db.JSON)
  params=db.Column(db.JSON)
  token=db.Column(db.String(128))
  token_expire=db.Column(db.DateTime)

# class UICase(db.Model):
#   __tablename__='ui_case'

class Department(db.Model):
  __tablename__ = 'department'
  department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  department_name = db.Column(db.String(20), unique=True)
  # users_of_department = db.relationship('User', backref='Department', lazy='dynamic')

  def __repr__(self):
   return '<Role %r>' % self.department_name

class Task(db.Model):
  __tablename__ = 'task'
  task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  task_name = db.Column(db.String(50))
  user_id = db.Column(db.Integer)
  case_id = db.Column(db.Integer)
  auth = db.Column(db.Boolean, default=True)
  task_time = db.Column(db.DateTime)