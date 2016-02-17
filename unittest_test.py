import unittest
from ThousandEyesPY import ThousandEyesPY
from ThousandEyesPY.exceptions import AuthenticationException


class TestThousandEyesPYMethods(unittest.TestCase):
    """docstring for TestThousandEyesPYMethods"""
    def test_agent_list(self):
        "Test Agent Updates"
        api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
        agent_list = api.agent_list()
        self.assertTrue(isinstance(agent_list, dict))

    def test_agent_list_bad_auth(self):
        "Test Agent list with Bad Auth"
        with self.assertRaises(AuthenticationException) as context:
            api = ThousandEyesPY(username="noreply@.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
            api.alert_rules()
        self.assertTrue('Bad Authentication' in str(context.exception))

    def test_test_list(self):
        "Test Test List Grab"
        api = ThousandEyesPY(username="noreply@.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
        test_list = api.test_list()
        self.assertTrue(isinstance(test_list, dict))

    def test_test_type_list(self):
        "Test Test List by type Grab"
        api = ThousandEyesPY(username="noreply@.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
        test_list = api.test_list(type="bgp")
        self.assertTrue(isinstance(test_list, dict))

if __name__ == '__main__':
    unittest.main()
