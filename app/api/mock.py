#coding=gbk
from datetime import datetime
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .auth import generate_token, confirm_token

bp = Blueprint('mock', __name__, url_prefix='/mock')

@bp.route('/github/<test>', methods=['GET','POST'])
def github(test):
  token = request.headers.get('Authorization')
  if token is not None:
    return jsonify(dict(testenv='mock',end_point=test,token=token.split(' ')[-1],valid_token=confirm_token(current_app.config['SECRET_KEY'],test,token)))
  return jsonify(dict(testenv='mock',end_point=test,valid_token=False))
