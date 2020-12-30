from flask import Flask,request,current_app,abort,render_template
from flask_bootstrap import Bootstrap 
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
  data = (1,2,3,4,5)
  return render_template('index.html',data=data)

@app.route('/user/<name>')
def user(name):
  return render_template('user.html',name=name)

@app.route('/login')
def name():
  return render_template('login.html',name=name)

@app.route('/test/<input>')
def test(input):
  if input == 'abort':
    return abort(404)
  return '<h1>test: %s </h1>' % input

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500

if __name__ == '__main__':
  app.run(debug=True)
