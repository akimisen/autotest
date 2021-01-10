#coding=gbk
from .. import db
from ..models import User,CaseInfo,Task
from ..components.forms import RestCaseForm

from flask import Blueprint, flash, redirect, render_template, session, url_for
from flask_login import login_user,login_required,current_user

from datetime import datetime
import time

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/list/user', methods=['GET'])
def query_user_tasks():
  # tasks = Task.query.filter_by(user_id=current_user.get_id())
  # return render_template('tasklist.html',tasks=tasks)
  return render_template('tasklist.html')

    # page = request.args.get('page', 1, type=int)
    # pagination = Message.query.paginate(page, per_page=10)
    # messages = pagination.items
    # titles = [('id', '#'), ('text', 'Message'), ('author', 'Author'), ('category', 'Category'), ('draft', 'Draft'), ('create_time', 'Create Time')]
    # return render_template('table.html', messages=messages, titles=titles)

@bp.route('/add', methods=['POST'])
def add_task():
  tasks = Task.query.filter_by(user_id=current_user.get_id())
  return render_template('tasklist.html',tasks=tasks)

@bp.route('/view/<int:task_id>', methods=['GET'])
def view_task():
  tasks = Task.query.filter_by(user_id=current_user.get_id())
  return render_template('tasklist.html',tasks=tasks)

@bp.route('/delete/<int:task_id>', methods=['DELETE'])
def edit_task(task_id):
  tasks = Task.query.filter_by(user_id=current_user.get_id())
  return render_template('tasklist.html',tasks=tasks)
