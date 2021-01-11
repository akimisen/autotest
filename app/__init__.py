#coding=gbk
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# import pymysql
from flask_migrate import Migrate

#init flask with plugins
bootstrap = Bootstrap()
moment = Moment()
# pymysql.install_as_MySQLdb()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message = '请登录后访问该页面'

def create_app():
  app = Flask(__name__)
  # from config import config
  # app.config.from_object(config[config_name])
  # config[config_name].init_app(app)
  # app.config['SQLALCHEMY_DATABASE_URI']='mysql://tracy:Test_123@localhost/test'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
  app.config['SECRET_KEY']='default key'
  app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'cosmo'
  app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'  
  bootstrap.init_app(app)
  moment.init_app(app)
  db.init_app(app)
  migrate = Migrate(app, db)
  login_manager.init_app(app)
  from .views import user,case,task,project,env
  from .api import routes as api,mock
  app.register_blueprint(user.bp)
  app.register_blueprint(project.bp)
  app.register_blueprint(env.bp)
  app.register_blueprint(case.bp)
  app.register_blueprint(task.bp)
  app.register_blueprint(api.bp)
  app.register_blueprint(mock.bp)
  return app