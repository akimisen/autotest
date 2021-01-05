#coding=gbk
from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, session, url_for
from . import db
from .forms import RestCaseForm
from .models import User,RestCase,CaseInfo
from flask_login import login_user,login_required,current_user

bp = Blueprint('case', __name__, url_prefix='/case')

@bp.route('/editor/<case_model>', methods=['GET','POST'])
def case_editor(case_model):
  if case_model == 'api':
    form = RestCaseForm()
    user = User.query.get(current_user.get_id())
    if user is None:
      flash("cookie失效请重新登录")
      return redirect(url_for('/'))
    if form.validate_on_submit():
      # if Case.exists(form.case_name.data.strip()):
      caseinfo = CaseInfo(group_id=user.group_id,user_id=user.user_id,project_id=form.project_id.data,case_model=case_model,case_description=form.case_description.data)
      restcase = RestCase(url=form.url.data,method=form.method.data,params=form.params.data,headers=form.headers.data)
      db.session.add(caseinfo)
      db.session.add(restcase)
      db.session.commit()
      return redirect(url_for('case.caselist'))
    return render_template('case-editor.html',case_model=case_model,form=form,user=user)
  elif case_model == 'ui':
    # form = UICaseForm()
    return '<h1>ui case model...</h1>'
  return render_template('404.html')

@bp.route('/list', methods=['GET','POST'])
def caselist():
  # cases = CaseInfo.query.filter_by(user_id=current_user.get_id())
  # cases = CaseInfo.query.order_by(updated_time)
  # result = dict(case_id=case.case_id,case_name=case.case_name,case_)
  return render_template('ajax.html')


