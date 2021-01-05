from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
import pymysql

bootstrap = Bootstrap()
moment = Moment()
pymysql.install_as_MySQLdb()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
pagedown = PageDown()

def create_app():
  app = Flask(__name__)
  # from config import config
  # app.config.from_object(config[config_name])
  # config[config_name].init_app(app)
  app.config['SQLALCHEMY_DATABASE_URI']='mysql://tracy:Test_123@localhost/test'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
  app.config['SECRET_KEY']='default key'
  bootstrap.init_app(app)
  moment.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)
  pagedown.init_app(app)
  from . import userview,caseview,taskview,mocker,api
  app.register_blueprint(userview.bp)
  app.register_blueprint(caseview.bp)
  app.register_blueprint(taskview.bp)
  app.register_blueprint(mocker.bp)
  app.register_blueprint(api.bp)
  return app