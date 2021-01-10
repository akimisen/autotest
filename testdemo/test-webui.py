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

""" ��Context��ʵ��case���е������Ĺ���
    ��װ��web-ui�Զ����ľ���ʵ�ַ������򻯰�
    ������Ҫ��һ���ֲ㣬����selenium��api֧�ֵĹ����ࣨdriver,element,wait,key�ȣ����в��
    ����Ҫ�Դ򿪡��ر����������������й�����֤������ر�
    �����ʵ����chrome """
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
      raise NotImplementedError('��λ��ʽ find_element_by_%s δʵ��' % (by))
    if by == 'id':
      return self.driver.find_element_by_id(value)
    if by == 'xpath':
      return self.driver.find_element_by_xpath(value)
    if by == 'css':
      return self.driver.find_element_by_css_selector(value)
    if by == 'linktext':
      return self.driver.find_element_by_id(value)

  """ У��Ԫ�ؿɼ���
      ����У�鶨λ������Ψһ�Ե�...   """
  def is_visible(self,by,value):
    return EC.visibility_of(self.find_element_by(by,value))

  def send_keys(self,by,value,key):
    if is_visible(self.find_element_by(by,value)):
      self.find_element_by(by,value).send_keys(key)

  """��ʾ�ȴ�&��ʽ�ȴ�"""
  def wait_util_element_visible(self,by,value,timeout):
    Wait(self.driver,timeout).until(EC.visibility_of_element_located(by,value))

  def wait_util_element_clickable(self,by,value,timeout):
    Wait(self.driver,timeout).until(EC.element_to_be_clickable(by,value))

  def wait_for_seconds_implicitly(self,timeout):
    self.implicitly_wait = driver.implicitly_wait(timeout)

  """����ҳ����ת
    redirect"""
  def redirect(self,last_step,old_url):
    #��֤ǰ������
    if not last_step['func'].startswith('wait_util'):
      print('ҳ����ת<%s>ǰ��Ҫ���õȴ�' % old_url)
    elif self.driver.current_url.strip() == old_url:
      time.sleep(1)
      if self.driver.current_url.strip() == old_url:
        print('����ʧ��')

  """����iframe,�����л���"""
  def switch(self):
    pass

  """Ԥ�ڽ������У�鷽��Ϊĳ��Ԫ�ص�ĳ������"""
  def verify_by_element_attribute(self,by,by_value,attr):
    if is_visible(by,by_value):
      element = self.driver.find_element_by(by,by_value)
      self.result = element.get_attribute(attr)
    else:
      pass

  """У�鷽��Ϊĳ��Ԫ�ص�����"""
  def verify_by_element_text(self,by,by_value):
    if is_visible(by,by_value):
      element = self.driver.find_element_by(by,by_value)
      self.result = element.text
    else:
      pass

  """У�鷽��Ϊ��ǰҳ��title"""
  def verify_by_title(self):
    return driver.title

  def close_session(self,driver):
    driver.quit()


"""http�ӿ�ʵ��"""

# def get(url,pararms,headers):
#   pass

# def post(url,data,headers):
#   pass


"""---------------"""
"""------main-----"""
"""---------------"""

"""ͨ���Զ�������ƽ̨¼���������ݣ����߰�excelά���İ����������������
  ����ʱ��ȡdb���˴�Ϊ�������ݣ�action��Ϊ����ĺ�����&����"""
steps = [
  dict(name='case001',case_id=1,step_id=0,action=('init_driver','chrome')),
  dict(name='case001',case_id=1,step_id=1,action=('create_session','http://www.baidu.com')),
  dict(name='case001',case_id=1,step_id=2,action=('send_key','css','#kw','��������xxxx')),
  dict(name='case001',case_id=1,step_id=3,action=('wait_until_element_visible','css','#kw')),
  dict(name='case001',case_id=1,step_id=3,action=('verify_by_title'), expected_result = '�ٶ�һ�£����֪��'),
  dict(name='case001',case_id=1,step_id=3,action=('close_session'))
]
driver_name='Chrome'
case_id=1

class MyTestCase(unittest.TestCase):

  def setUp(self):
    pass

  """������action�еĹؼ��֣�ӳ�䵽ͬ�����ຯ��"""
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
          result='��֧�ָùؼ��� %s'% method
    else:
      result='������Ϣδ����Ԥ�ڽ�� case_id=%s' % case_id
    self.assertEqual(result, expected_result)

def run_test(report_path):
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase)
  with open(report_path,'w') as f:
    runner = unittest.TextTestRunner(stream=f,descriptions=True,verbosity=2)
    runner.run(suite)
    unittest.main()

run_test('report-web-ui.txt')