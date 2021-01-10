#coding=gbk
from .. import db
from ..models import User
from ..components.forms import LoginForm

from flask import Blueprint, flash, redirect, render_template, session, url_for
from flask_login import login_user,login_required,current_user,logout_user

from datetime import datetime

bp = Blueprint('user', __name__)

@bp.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(user_name=form.user_name.data).first()
    if user is not None and user.check_password(form.password.data):
      login_user(user, form.if_remember.data)
      return redirect(url_for('case.query_user_cases'))
    elif user is None:
      user = User(user_name=form.user_name.data,password=form.password.data,group_id=form.group_id.data)
      db.session.add(user)
      db.session.commit()
      login_user(user, form.if_remember.data)
      flash("注册成功!",'success')
      return redirect(url_for('case.query_user_cases'))
    else:
      flash('用户名或密码错误!','warning')
  # flash('输入信息有误!')
  return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('.login'))

@bp.route('/dashboard')
def dashboard():
  user = User.query.get(current_user.get_id())
  if user:
    return render_template('dashboard.html' , user_name=user.user_name)
