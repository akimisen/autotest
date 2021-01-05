#coding=gbk
from datetime import datetime
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from . import db
from .forms import TaskForm
from .models import User,CaseInfo,RestCase,Task
from flask_login import login_user,login_required,current_user
import time
from ddt import ddt,data,unpack
from datetime import datetime

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/manager/', methods=['GET','POST'])
def task_manager():
  return '<h1>task-manager...</h1>'

@bp.route('/list', methods=['GET','POST'])
def tasklist():
  tasks = Task.query.filter_by(user_id=current_user.get_id())
  return render_template('tasklist.html',tasks=tasks)

@bp.route('/run/case/<case_id>')
def run_case(case_id):
  case = CaseInfo.query.get(case_id)
  # rest_case = RestCase.query.get(case_id)
  task_time = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
  task = Task(user_id=current_user.get_id(),task_name=case.case_description+'_'+task_time,task_time=task_time)
  db.session.add(task)
  db.session.commit()
  #run test script
  return '<h1> 任务已执行,名称： %s  </h1>' % task.task_name

@bp.route('/run/cases/<cases>')
def run_cases(cases):
  pass
