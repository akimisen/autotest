#coding=gbk
from .. import db
from ..models import User,CaseInfo,RestCase,WebCase
from ..components.forms import RestCaseForm, WebCaseForm

from flask import Blueprint, flash, request, redirect, render_template, session, url_for
from flask_login import login_required,current_user

from datetime import datetime

bp = Blueprint('case', __name__, url_prefix='/case')

@bp.route('/all', methods=['GET'])
@login_required
def query_all_cases():
  page = request.args.get('page', 1, type=int)
  pagination = CaseInfo.query.order_by(CaseInfo.updated_at.desc()).paginate(page, per_page=10)
  cases = pagination.items
  titles = [('case_id','case_id'),('case_name', '用例名称'),('project_id', '项目id'), ('created_at', '创建时间'), ('updated_at','更新时间')]
  form=RestCaseForm()
  return render_template('caselist.html', pagination=pagination, cases=cases, titles=titles, form=form)

@bp.route('/user', methods=['GET','POST'])
@login_required
def query_user_cases():
  # for i in range(0,10):
  #   case = CaseInfo(case_name='case-name-test00%d'%i,owner_id=1,case_desc='case-desc-test00%d'%i,project_id=2,updated_at=datetime.now(),created_at=datetime.now())
  #   rest_case=RestCase(url='/github/00%d'%i,method='GET')
  #   db.session.add(case,rest_case)
  #   db.session.commit()
  page = request.args.get('page', 1, type=int)
  user = User.query.get(current_user.id)
  if user:
    pagination = CaseInfo.query.filter_by(owner_id=user.user_id).order_by(CaseInfo.updated_at.desc()).paginate(page, per_page=10)
    cases = pagination.items
    titles = [('case_id','case_id'),('case_name', '用例名称'),('project_id', '项目id'), ('created_at', '创建时间'), ('updated_at','更新时间')]
    form=RestCaseForm()
    return render_template('caselist.html', pagination=pagination, cases=cases, titles=titles, form=form)
  return render_template('500.html')

@bp.route('/add/case/http', methods=['GET','POST'])
@login_required
def add_case_http():
  case_model='http'
  form = RestCaseForm()
  user = User.query.get(current_user.get_id())
  if form.validate_on_submit():
    if CaseInfo.query.filter_by(project_id=form.project_id.data,case_name=form.case_name.data,owner_id=user.user_id).first():
      flash("您已为该项目创建过同一名称的用例，请修改!",'warning')
    else:
      try:
        caseinfo = CaseInfo(group_id=user.group_id,owner_id=user.user_id,project_id=form.project_id.data,case_name=form.case_name.data,case_model=case_model,case_desc=form.case_desc.data,updated_at=datetime.now(),created_at=datetime.now())
        restcase = RestCase(url=form.url.data,method=form.method.data,params=form.params.data,headers=form.headers.data)
        db.session.add(caseinfo)
        db.session.add(restcase)
        db.session.commit()
        flash('提交成功','success')
        return redirect(url_for('case.query_user_cases'))
      except:
        return render_template('500.html')
  return render_template('add_case.html',case_model=case_model,form=form)
  
@bp.route('/add/case/web', methods=['GET','POST'])
@login_required
def add_case_web():
  pass