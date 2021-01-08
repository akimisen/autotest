class Config(dict):
  """methods to set task configs:
    sql:
      task.config.from_sql(db_connection,sql)
    or from a ini_file:
      task.config.from_ini(ini)
  """

  def __init__(self, defaults=None):
    dict.__init__(self, defaults or {})

  def from_sql(self,db,sql):
    pass

  def from_ini(self,file):
    pass