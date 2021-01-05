from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, session, url_for
from . import db
from .forms import RestCaseForm
from .models import User,RestCase,CaseInfo
from flask_login import login_user,login_required,current_user

bp = Blueprint('env', __name__, url_prefix='/env')

@bp.route('/list', methods=['GET'])
def env_list():
  pass
  