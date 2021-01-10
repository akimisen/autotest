import unittest
import requests

steps = [dict(method='GET',url='http://www.baidu.com',headers={},status_code='200') for i in range(5)]
class MyTestCase(unittest.TestCase):

  steps=steps

  def setUp(self):
    pass
  
  def test_requests(self):
    for step in self.steps:
      res = requests.get(url=step['url'],headers=step['headers'])
      with self.subTest(i=steps.index(step)):
        self.assertEqual(str(res.status_code), step['status_code'])
  
  def tearDown(self):
    pass

def run_test(report_path):
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase)
  with open(report_path,'w') as f:
    runner = unittest.TextTestRunner(stream=f,descriptions=True,verbosity=2)
    runner.run(suite)
    unittest.main()

run_test('report-http.txt')
  
