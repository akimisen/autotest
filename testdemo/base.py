#coding=gbk
from utils.io import read_info, read_contents_web
"""����Case���࣬����case��Ҫ�õ��ĳ�Ա�����ͷ���"""

class Case:
  def __init__(self,model):
    # models = ('http','web_ui','app_ui')
    self.model=model

class WebUICase(Case):
  def __init__(self):
    super().__init__('web_ui')

  #���ݿ��ȡ����caseͨ����Ϣ: id,name,desc
  @property
  def info(self,case_id):
    return self._info
  
  @info.setter
  def info(self,db,case_id):
    self._info = read_info(db,case_id) 

  #���ݿ��ȡ����case�����������
  @property
  def contents(self):
    return self._contents
  
  @contents.setter
  def contents(self,db,case_id):
    self._contents = read_contents_web(db,case_id)

class HTTPCase(Case):
  def __init__(self,name,owner,desc,**contents):
    super().__init__('http')
    self.name=name
    self.owner=owner
    self.desc=desc
    if contents.get('method'):
      self.method=contents.method
    

# case = WebUICase(1,2,3,4,5,6)
# case.info = read_info()
# print(case.info())
