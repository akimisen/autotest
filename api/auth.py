from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def generate_token(key, id, expire=3600):
  s = Serializer(key, expire) 
  return s.dumps({'token': id})

def confirm_token(key, id, token):
  s = Serializer(key)
  try:
    data = s.loads(token)
  except:
    return False
  if data.get('token') != id:
    return False
  return True