# from .config import Config

class Task:

  config_class = Config
  default_config = {
    'HTTP_HOST_DEFAULT': 'localhost:5000',
    'WEBDRIVER_WAIT_SECONDS': 10,
    'ENABLE_TOKEN_GENERATION': True,
  }

  def __init__(self,task_id):
    self.task_id=task_id
  
  def set_config(self):
    return self.config_class(self.default_config)

  def run(self):
    pass