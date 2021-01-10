#coding=gbk
from .. import db
from ..models import User,CaseInfo,RestCase
from ..components.forms import RestCaseForm

from flask import Blueprint, flash, redirect, render_template, session, url_for
from flask_login import login_user,login_required,current_user

from datetime import datetime

bp = Blueprint('env', __name__, url_prefix='/env')

@bp.route('/list', methods=['GET'])
def query_user_envs():
  return render_template('env.html')
  