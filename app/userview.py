#coding=gbk
from datetime import datetime
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from . import db
from .forms import LoginForm
from .models import User
from flask_login import login_user,login_required,current_user

bp = Blueprint('user', __name__, url_prefix='/')

@bp.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(user_name=form.user_name.data).first()
    if user is not None and user.check_password(form.password.data):
      login_user(user, form.if_remember.data)
      return redirect(url_for('user.home'))
    elif user is None:
      user = User(user_name=form.user_name.data,password=form.password.data,group_id=form.group_id.data)
      db.session.add(user)
      db.session.commit()
      login_user(user, form.if_remember.data)
      return redirect(url_for('user.home'))
    else:
      flash('用户名或密码错误!')
  # flash('输入信息有误!')
  return render_template('login.html', form=form)

@bp.route('/home')
@login_required
def home():
  return render_template('home.html' , user_name=User.query.get(current_user.get_id()).user_name )

