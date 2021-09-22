from dataclasses import dataclass, field
import unittest
from unittest import mock
from crazy_script import CrazyScript
from urllib.parse import urlparse

@dataclass
class MockRequest:
    status_code: int
    result: dict = field(default_factory=dict)

    def json(self):
        return self.result

class CrazyScripTestCase(unittest.TestCase):
    def test_process_age(self):
        cs = CrazyScript()
        cs.element = {
            "age": 18,
        }
        age = cs.process_age()
        self.assertEqual(age, "Adult")
        cs.element = {
            "age": 0,
        }
        age = cs.process_age()
        self.assertEqual(age, "Baby")
        cs.element = {
            "age": 10,
        }
        age = cs.process_age()
        self.assertEqual(age, "Child")
    
    def test_process_account(self):
        cs = CrazyScript()
        cs.element = {
            "age": 10,
        }
        age = cs.process_age()
        self.assertEqual(age, "Child")
    
    @mock.patch('requests.get')
    def test_populate_data(self, mock_request):
        cs = CrazyScript()
        result = {
            "age": 10,
            "name": "John",
            "account": {
                "enabled": False
            }
        }
        mock_request.return_value = MockRequest(status_code=200, result=result)
        cs.populate('/')
        self.assertDictEqual(cs.element, {
            "age": 10,
            "account": {
                "enabled": False
            }
        })
    
    @mock.patch('requests.get')
    def test_populate_data_2(self, mock_request):
        cs = CrazyScript()
        result = {
            "error": "You did something wrong"
        }
        mock_request.return_value = MockRequest(status_code=500, result=result)
        self.assertRaises(Exception, cs.populate, '/')


class RequestTestCase(unittest.TestCase):
    def test_connection_api_wrong(self):
        cs = CrazyScript()
        self.assertRaises(Exception, cs.populate, '/')
    
    def test_connection_api_good(self):
        cs = CrazyScript()
        cs.populate('/some_user')
        self.assertEqual(cs.element, {
            "age": 3,
            "account": {
                "enabled": False
            }
        })

if __name__ == '__main__':
    unittest.main()
