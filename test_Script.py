import unittest

class TestScript(unittest.TestCase):
    def test_output(self):
        self.assertEqual("Hello from GitHub!", "Hello from GitHub!")

if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
