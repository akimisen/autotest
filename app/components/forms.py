#coding=gbk
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
  user_name = StringField('�û���:', validators=[DataRequired(),Length(1,20)])
  password = PasswordField('����:', validators=[DataRequired()])
  group_id = SelectField(label='��ѡ����Ŀ��:' ,validators=[DataRequired()], choices=((1,'��1'),(2,'��2'),(3,'��3')), default=1)
  if_remember = BooleanField('�Ƿ񱣳ֵ�¼״̬?', default=True)
  submit = SubmitField('��¼\ע��')

class RestCaseForm(FlaskForm):
  project_id = SelectField(label='ѡ����Ŀ:', choices=((1,'��Ŀ1'),(2,'��Ŀ2'),(3,'��Ŀ3')), default=1)
  case_name = StringField(label='��������:', validators=[Length(1,50)])
  case_desc = TextAreaField(label='��������:', validators=[Length(1,100)])
  url = StringField(label='url:', validators=[DataRequired(), Length(1,100)])
  method = SelectField(label='method:', choices=((1,'GET'),(2,'POST'),(3,'PUT'),(4,'DELETE')), default=1)
  params = StringField(label='params:')
  headers = StringField(label='headers:')
  data = StringField(label='data:')
  submit = SubmitField('�ύ')

class WebCaseForm(FlaskForm):
  pass

class TaskForm(FlaskForm):
  env = SelectField(label='ѡ�񻷾�:', choices=((1,'Mock'),(2,'����'),(3,'����')), default=1)
  configs = StringField('ģ������:', validators=[Length(1,1000)])
  url = StringField('url:', validators=[Length(1,100)])
  method = RadioField(label='method:', choices=((1,'GET'),(2,'POST'),(3,'OPTION'),(4,'DELETE')), default=1)
  params = StringField('params:')
  headers=StringField('headers:')
  submit = SubmitField('�ύ')

