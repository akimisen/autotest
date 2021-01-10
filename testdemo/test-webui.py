#coding=gbk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WWait
from selenium.webdriver.support import expected_conditions as EC

class Env:
  def __init__(self, driver_name='Chrome',options=None, wait=None):
    if str.capitalize(driver_name) == 'Chrome':
      self.driver = webdriver.Chrome(options=options)
    self.wait=wait
  
  def create_session(self,start_url):
    if self.driver:
      self.driver.get(start_url)

  def send_keys(self,by,value,key):
    if EC.visibility_of_element_located(by,value):
      self.driver.find_element(by,value).send_keys(key)

  def wait_util_element_visible(self,by,value,timeout):
    WWait(self.driver,timeout).until(EC.visibility_of_element_located(by,value))

  def wait_util_element_clickable(self,by,value,timeout):
    WWait(self.driver,timeout).until(EC.element_to_be_clickable(by,value))

  def get_result_by_title(self,by,value,attr):
    if self.driver:
      return self.driver.title

class Step:
  def __init__(self,case_id,step_id,conditions,method_kw,params,return_type=None,expected_result=None):
    self.case_id=case_id
    self.step_id=step_id
    self.conditions = conditions
    self.method_kw = method_kw
    self.params = params
    self.return_type = return_type
    self.expected_result = expected_result
  
  def run(self, env):
    assert all(self.conditions) == True, 'step %d, %s 运行失败,前提条件不能都满足: %s' % (self.step_id, self.method_kw, self.conditions)
    assert getattr(env.__class__,method_kw) and callable(getattr(env.__class__,method_kw)), 'step %d, %s 运行失败, 未实现方法%s' % (self.step_id, self.method_kw)
    method_to_call = getattr(env.__class__,method_kw)
    if params is None:
      if self.return_type is None:
        try:
          method_to_call(env.__class__)
        except (TypeError,ValueError) as e:
          print('step %d, %s 运行失败, 参数错误: %s' % (self.step_id, self.method_kw, e))
        except Exception as e:
          print(e)
      elif self.return_type== 'result' and expected_result is not None:
        result = method
        setattr(env.__class__,'actual_result',)
    else:
      try:
        method_to_call(env.__class__, pa)
      except (TypeError,ValueError) as e:
        print('step %d, %s 运行失败, 参数%s错误: %s' % (self.step_id, self.method_kw, self.params, e))
      except Exception as e:
        print(e)

class Case:
  def __init__(self,name,cid):
    self.name=name
    self.id=cid
    self.steps=[]
    self.result_step=None

  def load_steps(self, data):
    for d in data:
      step = Step(**d)
      self.steps.append(step)
      if step.return_type == 'result' and step.expected_result is not None:
        self.result_step = step.step_id
  
  def run_steps(self, context):
    for s in steps:
      step.run(context)
  
steps = [
  dict(name='case001',case_id=1,step_id=0,action=('init_driver','chrome')...
  dict(name='case001',case_id=1,step_id=1,action=('create_session','http://www.baidu.com')),
  dict(name='case001',case_id=1,step_id=2,action=('send_key','css','#kw','搜索内容xxxx')),
  dict(name='case001',case_id=1,step_id=3,action=('wait_until_element_visible','css','#kw')),
  dict(name='case001',case_id=1,step_id=3,action=('get_result_by_title'), expected_result = '百度一下，你就知道'),
  dict(name='case001',case_id=1,step_id=3,action=('close_session'))
]