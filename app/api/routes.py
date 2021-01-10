#coding=gbk
from ..models import CaseInfo
from .. import db

from flask import Blueprint, render_template, request, url_for, jsonify
# from .auth import generate_token, confirm_token
from flask_login import current_user

from datetime import datetime

bp = Blueprint('api', __name__, url_prefix='/api')

#res.setHeader('Access-Control-Allow-Origin', '*');

@bp.route('/case/all', methods=['GET'])
def query_all_cases():
  cases = CaseInfo.query.all()
  result = [dict(key=case.case_id,href=url_for('.query_case_all'),name=case.case_name,owner='owner111',desc=case.case_description,model=case.case_model,updatedAt=datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')) for case in cases]
  return jsonify(result)

@bp.route('/case/user', methods=['GET','POST'])
def query_user_cases():
  print(request.headers.get('Content-Type'))
  cases = CaseInfo.query.filter_by(user_id=1)
  case = cases.first()
  result = dict(key=case.case_id,href=url_for('.query_case_all'),name=case.case_name,owner='owner111',desc=case.case_description,model=case.case_model,updatedAt=datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'))
  if result:
    return jsonify(result)

@bp.route('/currentUser', methods=['GET','POST'])
def query_user():
  return (jsonify(dict(user=current_user)))

@bp.route('/case/add', methods=['GET','POST'])
def add_case():
  return (jsonify(dict(user=current_user)))


