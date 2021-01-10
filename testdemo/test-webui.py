#coding=gbk

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import unittest

#from functools import wraps
#from .enums import *

""" 用Context类实现case运行的上下文管理
    封装了web-ui自动化的具体实现方法，简化版
    可能需要进一步分层，按照selenium的api支持的工具类（driver,element,wait,key等）进行拆分
    还需要对打开、关闭浏览器这类操作进行管理，保证结束后关闭
    这里仅实现了chrome """
class Context(Type):
  def __init__(self,driver_name,option=None,implicitly_wait=0):
    if str.capitalize(driver_name)=='Chrome':
      self.driver=webdriver.Chrome()
      # self.elements=[]
      if implicitly_wait>0:
        self.implicitly_wait=implicitly_wait
        driver.implicitly_wait(self.implicitly_wait)

  def create_session(self,start_url):
    if self.driver:
      self.driver.get(start_url)

  def find_element_by(self,by,value):
    if by not in ('id','xpath','css','linktext'):
      raise NotImplementedError('定位方式 find_element_by_%s 未实现' % (by))
    if by == 'id':
      return self.driver.find_element_by_id(value)
    if by == 'xpath':
      return self.driver.find_element_by_xpath(value)
    if by == 'css':
      return self.driver.find_element_by_css_selector(value)
    if by == 'linktext':
      return self.driver.find_element_by_id(value)

  """ 校验元素可见性
      还需校验定位方法的唯一性等...   """
  def is_visible(self,by,value):
    return EC.visibility_of(self.find_element_by(by,value))

  def send_keys(self,by,value,key):
    if is_visible(self.find_element_by(by,value)):
      self.find_element_by(by,value).send_keys(key)

  """显示等待&隐式等待"""
  def wait_util_element_visible(self,by,value,timeout):
    Wait(self.driver,timeout).until(EC.visibility_of_element_located(by,value))

  def wait_util_element_clickable(self,by,value,timeout):
    Wait(self.driver,timeout).until(EC.element_to_be_clickable(by,value))

  def wait_for_seconds_implicitly(self,timeout):
    self.implicitly_wait = driver.implicitly_wait(timeout)

  """处理页面跳转
    redirect"""
  def redirect(self,last_step,old_url):
    #验证前置条件
    if not last_step['func'].startswith('wait_util'):
      print('页面跳转<%s>前需要设置等待' % old_url)
    elif self.driver.current_url.strip() == old_url:
      time.sleep(1)
      if self.driver.current_url.strip() == old_url:
        print('操作失败')

  """处理iframe,窗口切换等"""
  def switch(self):
    pass

  """预期结果处理，校验方法为某个元素的某个属性"""
  def verify_by_element_attribute(self,by,by_value,attr):
    if is_visible(by,by_value):
      element = self.driver.find_element_by(by,by_value)
      self.result = element.get_attribute(attr)
    else:
      pass

  """校验方法为某个元素的文字"""
  def verify_by_element_text(self,by,by_value):
    if is_visible(by,by_value):
      element = self.driver.find_element_by(by,by_value)
      self.result = element.text
    else:
      pass

  """校验方法为当前页面title"""
  def verify_by_title(self):
    return driver.title

  def close_session(self,driver):
    driver.quit()


"""http接口实现"""

# def get(url,pararms,headers):
#   pass

# def post(url,data,headers):
#   pass


"""---------------"""
"""------main-----"""
"""---------------"""

"""通过自动化测试平台录入以下数据，或者把excel维护的案例整理好批量导入
  运行时读取db，此处为测试数据，action列为上面的函数名&参数"""
steps = [
  dict(name='case001',case_id=1,step_id=0,action=('init_driver','chrome')),
  dict(name='case001',case_id=1,step_id=1,action=('create_session','http://www.baidu.com')),
  dict(name='case001',case_id=1,step_id=2,action=('send_key','css','#kw','搜索内容xxxx')),
  dict(name='case001',case_id=1,step_id=3,action=('wait_until_element_visible','css','#kw')),
  dict(name='case001',case_id=1,step_id=3,action=('verify_by_title'), expected_result = '百度一下，你就知道'),
  dict(name='case001',case_id=1,step_id=3,action=('close_session'))
]
driver_name='Chrome'
case_id=1

class MyTestCase(unittest.TestCase):

  def setUp(self):
    pass

  """处理案例action中的关键字，映射到同名的类函数"""
  def test_steps(self):
    context=Context(driver_name)
    if steps[-2].get('action').startswith('verify') and steps[-2].get('expected_result'):
      expected_result = steps[-2].get('result').strip()
      for step in self.steps:
        method = step.get('action')[0]
        params = None if len(step)<=1 else step.get('action')[1:]
        if getattr(Context,method) and callable(getattr(Context,method)):
          method_to_call = getattr(Context,method)
          if not step.get('action').startswith('verify'):
            if params:
              method_to_call(context,*params)
            else:
              method_to_call(context)
          else:
            if params:
              result = method_to_call(context,*params)
            else:
              result = method_to_call(context)
        else:
          result='不支持该关键字 %s'% method
    else:
      result='用例信息未包含预期结果 case_id=%s' % case_id
    self.assertEqual(result, expected_result)

def run_test(report_path):
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase)
  with open(report_path,'w') as f:
    runner = unittest.TextTestRunner(stream=f,descriptions=True,verbosity=2)
    runner.run(suite)
    unittest.main()

run_test('report-web-ui.txt')