#coding=gbk
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
  user_name = StringField('用户名:', validators=[DataRequired(),Length(1,20)])
  password = PasswordField('密码:', validators=[DataRequired()])
  group_id = SelectField(label='请选择项目组:' ,validators=[DataRequired()], choices=((1,'组1'),(2,'组2'),(3,'组3')), default=1)
  if_remember = BooleanField('是否保持登录状态?', default=True)
  submit = SubmitField('登录\注册')

class RestCaseForm(FlaskForm):
  project_id = SelectField(label='选择项目:', choices=((1,'项目1'),(2,'项目2'),(3,'项目3')), default=1)
  case_name = StringField(label='用例名称:', validators=[Length(1,50)])
  case_desc = TextAreaField(label='用例描述:', validators=[Length(1,100)])
  url = StringField(label='url:', validators=[DataRequired(), Length(1,100)])
  method = SelectField(label='method:', choices=((1,'GET'),(2,'POST'),(3,'PUT'),(4,'DELETE')), default=1)
  params = StringField(label='params:')
  headers = StringField(label='headers:')
  data = StringField(label='data:')
  submit = SubmitField('提交')

class WebCaseForm(FlaskForm):
  pass

class TaskForm(FlaskForm):
  env = SelectField(label='选择环境:', choices=((1,'Mock'),(2,'测试'),(3,'生产')), default=1)
  configs = StringField('模块配置:', validators=[Length(1,1000)])
  url = StringField('url:', validators=[Length(1,100)])
  method = RadioField(label='method:', choices=((1,'GET'),(2,'POST'),(3,'OPTION'),(4,'DELETE')), default=1)
  params = StringField('params:')
  headers=StringField('headers:')
  submit = SubmitField('提交')

