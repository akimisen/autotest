#coding=gbk
import os
import unittest
import logging
import requests
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from ddt import ddt,data,unpack


def generate_token(key, id, expire=3600):
  s = Serializer(key, expire) 
  return s.dumps({'token': id})

case = dict(
  method='GET',url='http://localhost:5000/github/test133',headers={'Authorization':'token TOKEN'}
)
cases = [case for i in range(3)]

class Mylist(list):
  pass

class MyClass:
  def __init__(self, **kwargs):
    for field, value in kwargs.items():
      setattr(self, field, value)

  def __eq__(self, other):
    return isinstance(other, dict) and vars(self) == other or \
         isinstance(other, MyClass) and vars(self) == vars(other)

  def __str__(self):
    return "TestObject %s" % vars(self)

def annotated(a, b):
  r = Mylist([a, b])
  setattr(r, "__name__", "test_%d_greater_than_%d" % (a, b))
  return r

def annotated2(listIn, name, docstring):
  r = Mylist(listIn)
  setattr(r, "__name__", name)
  setattr(r, "__doc__", docstring)
  return r

@ddt
class FooTestCase(unittest.TestCase):
  def test_undecorated(self):
    self.assertTrue(24>=20)

  @data(annotated(2, 1), annotated(10, 5))
  def test_greater(self, value):
    a, b = value
    self.assertGreater(a, b)

  @data(annotated2([2, 1], 'Test_case_1', """Test docstring 1"""),
      annotated2([10, 5], 'Test_case_2', """Test docstring 2"""))
  def test_greater_with_name_docstring(self, value):
    a, b = value
    self.assertGreater(a, b)
    self.assertIsNotNone(getattr(value, "__name__"))
    self.assertIsNotNone(getattr(value, "__doc__"))

if __name__ == '__main__':
  
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(FooTestCase)
  with open(os.path.abspath(os.path.dirname(__file__))+'repo','wb') as f:
    runner = unittest.TextTestRunner(stream=f,verbosity=2)
    runner.run(suite)
    unittest.main()
