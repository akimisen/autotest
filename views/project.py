#coding=gbk
from .. import db
from ..models import User,CaseInfo,RestCase
from ..components.forms import RestCaseForm

from flask import Blueprint, flash, redirect, render_template, session, url_for
from flask_login import login_user,login_required,current_user

from datetime import datetime

bp = Blueprint('project', __name__, url_prefix='/project')

@bp.route('/list', methods=['GET'])
def query_all_projects():
  return render_template('project.html')
  