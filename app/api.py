#coding=gbk
from datetime import datetime
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .auth import generate_token, confirm_token
from .models import CaseInfo

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/caselist', methods=['GET'])
def caselist_api():
  cases = CaseInfo.query.all()
  result = [dict(url=url_for('.caselist_api'),case_id=case.case_id,case_name=case.case_name,case_mode=case.case_model) for case in cases]
  return jsonify(result)