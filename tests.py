from ThousandEyesPY import ThousandEyesPY
from pprint import pprint


def test_agent_update():
    "Test Agent Updates"
    api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
    api.update_agent(966, agentName="my cool updated agent name", accounts=315)


def test_bgp_monitor_list():
    "Test bgp_monitor_list"
    api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
    bgp_monitor_list = api.bgp_monitor_list()
    pprint(bgp_monitor_list)
