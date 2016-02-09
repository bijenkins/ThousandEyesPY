from ThousandEyesPY import ThousandEyesPY
from pprint import pprint
import unittest

def test_agent_list():
    "Test Agent Updates"
    api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
    agent_list = api.agent_list()
    pprint(agent_list)

def test_agent_details():
    "Test Agent Updates"
    api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
    agent_details = api.agent_details(16769)
    pprint(agent_details)

def test_delete_agent():
    "Test Agent Updates"
    api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
    delete_agent = api.delete_agent(966)


def test_agent_update():
    "Test Agent Updates"
    api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
    api.update_agent(966, agentName="my cool updated agent name", accounts=315)


def test_bgp_monitor_list():
    "Test bgp_monitor_list"
    api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
    bgp_monitor_list = api.bgp_monitor_list()
    pprint(bgp_monitor_list)


class TestThousandEyesPYMethods(unittest.TestCase):
    """docstring for TestThousandEyesPYMethods"""
    def test_agent_list(self):
        "Test Agent Updates"
        api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
        agent_list = api.agent_list()
        self.assertTrue(isinstance(agent_list, dict))

if __name__ == '__main__':
    unittest.main()
def main():
    # test_agent_list()
    # test_agent_details()
    test_bgp_monitor_list()

if __name__ == "__main__":
    main()
