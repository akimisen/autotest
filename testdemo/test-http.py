import unittest
import requests

steps = [dict(method='GET',url='http://www.baidu.com',headers={},status_code='123') for i in range(5)]
class MyTestCase(unittest.TestCase):

  def setUp(self):
    pass
  
  def test_requests(self):
    count=0
    for step in steps:
      with self.subTest(step_id=count,url=step['url'],headers=step['headers']):
        res=requests.get(url=step['url'],headers=step['headers'])
        self.assertEqual(str(res.status_code),step['status_code'])
      count+=1

  def tearDown(self):
    pass

def run_test(report_path):
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase)
  with open(report_path,'w') as f:
    runner = unittest.TextTestRunner(stream=f,descriptions=True,verbosity=2)
    runner.run(suite)
    unittest.main()

if __name__ == "__main__":
  run_test('report-http.txt')
  
