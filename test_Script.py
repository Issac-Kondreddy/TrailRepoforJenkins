import unittest
import xmlrunner
import os

class TestScript(unittest.TestCase):
    def test_output(self):
        self.assertEqual("Hello from GitHub!", "Hello from GitHub!")

if __name__ == '__main__':
    # Ensure the directory exists
    os.makedirs('test-reports', exist_ok=True)

    # Run the tests and generate the XML report
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
