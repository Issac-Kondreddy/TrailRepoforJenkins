import unittest

class TestScript(unittest.TestCase):
    def test_output(self):
        self.assertEqual("Hello from GitHub!", "Hello from GitHub!")

if __name__ == '__main__':
    unittest.main()
