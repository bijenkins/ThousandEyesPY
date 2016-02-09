### <i class="icon-eye"></i> ThousandEyesPY

ThousandEyesPY is a Python Library for accessing the ThousandEyes API. The library uses requests to access the RESTful API located at http://developer.thousandeyes.com/.

It is currently a work in progress. Currently the "Alerts" are completed. Helper functions for optional parameters are nearly complete.

All functions return a dictionary that you can use as your wish.

Currently HTTP Exceptions are generated from requests.

**Active Alerts**:

```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> active_alerts = api.active_alerts()
>>> pprint(active_alerts)
{u'alert': [{u'active': 1,
             u'agents': [{u'active': 1,
                          u'agentId': 12,
                          u'agentName': u'Hong Kong',
                          u'dateStart': u'2012-12-13 13:15:00',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=12'},
                         {u'active': 1,
                          u'agentId': 16,
                          u'agentName': u'S\xe3o Paulo, Brazil',
                          u'dateStart': u'2012-12-13 13:15:05',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=16'},
                         {u'active': 2,
                          u'agentId': 25,
                          u'agentName': u'Cape Town, South Africa',
                          u'dateEnd': u'2014-02-11 01:44:04',
                          u'dateStart': u'2012-12-13 13:15:00',
                          u'metricsAtEnd': u'N/A (agent removed from test)',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=25'},
                         {u'active': 1,
                          u'agentId': 32,
                          u'agentName': u'London, UK',
                          u'dateStart': u'2012-12-13 13:15:00',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=32'},
                         {u'active': 1,
                          u'agentId': 146,
                          u'agentName': u'San Jose, CA',
                          u'dateStart': u'2013-01-31 05:52:48',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=146'}],
             u'alertId': 2783,
             u'apiLinks': [{u'href': u'https://api.thousandeyes.com/tests/822',
                            u'rel': u'related'},
                           {u'href': u'https://api.thousandeyes.com/dns/dnssec/822',
                            u'rel': u'data'}],
             u'dateStart': u'2012-12-13 13:15:00',
             u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783',
             u'ruleExpression': u'Error is present',
             u'ruleId': 301,
             u'ruleName': u'Default DNSSEC Alert Rule',
             u'testId': 822,
             u'testName': u'thousandeyes.com A',
             u'type': u'DNSSEC',
             u'violationCount': 6}],
 u'pages': {u'current': 1}}
>>>
```
**Alert Detail**:

```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> alert_detail = api.active_alert_detail(alert_id=2783)
>>> pprint(alert_detail)
{u'alert': [{u'active': 1,
             u'agents': [{u'active': 1,
                          u'agentId': 12,
                          u'agentName': u'Hong Kong',
                          u'dateStart': u'2012-12-13 13:15:00',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=12'},
                         {u'active': 1,
                          u'agentId': 16,
                          u'agentName': u'S\xe3o Paulo, Brazil',
                          u'dateStart': u'2012-12-13 13:15:05',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=16'},
                         {u'active': 2,
                          u'agentId': 25,
                          u'agentName': u'Cape Town, South Africa',
                          u'dateEnd': u'2014-02-11 01:44:04',
                          u'dateStart': u'2012-12-13 13:15:00',
                          u'metricsAtEnd': u'N/A (agent removed from test)',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=25'},
                         {u'active': 1,
                          u'agentId': 32,
                          u'agentName': u'London, UK',
                          u'dateStart': u'2012-12-13 13:15:00',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=32'},
                         {u'active': 1,
                          u'agentId': 146,
                          u'agentName': u'San Jose, CA',
                          u'dateStart': u'2013-01-31 05:52:48',
                          u'metricsAtEnd': u'',
                          u'metricsAtStart': u'Error details: "No DNSSEC public key(s) for thousandeyes.com A"',
                          u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783&agentId=146'}],
             u'alertId': 2783,
             u'apiLinks': [{u'href': u'https://api.thousandeyes.com/tests/822',
                            u'rel': u'related'},
                           {u'href': u'https://api.thousandeyes.com/dns/dnssec/822',
                            u'rel': u'data'}],
             u'dateStart': u'2012-12-13 13:15:00',
             u'permalink': u'https://app.thousandeyes.com/alerts/list/?__a=75&alertId=2783',
             u'ruleExpression': u'Error is present',
             u'ruleId': 301,
             u'ruleName': u'Default DNSSEC Alert Rule',
             u'testId': 822,
             u'testName': u'thousandeyes.com A',
             u'type': u'DNSSEC',
             u'violationCount': 6}]}
>>>
```

**Alert Rules**:
```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> alert_rules = api.alert_rules()
>>> pprint(alert_rules)
{u'alertRules': [{u'alertType': u'BGP',
                  u'default': 1,
                  u'expression': u'Reachability < 100%',
                  u'minimumSources': 2,
                  u'notes': u'',
                  u'notifyOnClear': 0,
                  u'recipient': [],
                  u'roundsBeforeTrigger': 1,
                  u'ruleId': 322,
                  u'ruleName': u'Default BGP Alert Rule'},
                 {u'alertType': u'DNS Server',
                  u'default': 1,
                  u'expression': u'Error is present',
                  u'minimumSources': 2,
                  u'notes': u'',
                  u'notifyOnClear': 0,
                  u'recipient': [u'noreply@thousandeyes.com'],
                  u'roundsBeforeTrigger': 1,
                  u'ruleId': 300,
                  u'ruleName': u'Default DNS Server Alert Rule'},
                 {u'alertType': u'DNS Trace',
                  u'default': 1,
                  u'expression': u'Error is present',
                  u'minimumSources': 2,
                  u'notes': u'',
                  u'notifyOnClear': 0,
                  u'recipient': [u'noreply@thousandeyes.com'],
                  u'roundsBeforeTrigger': 1,
                  u'ruleId': 299,
                  u'ruleName': u'Default DNS Trace Alert Rule'},
                 {...},
                 {u'alertType': u'Web Transaction',
                  u'default': 1,
                  u'expression': u'Error is present',
                  u'minimumSources': 2,
                  u'notes': u'',
                  u'notifyOnClear': 0,
                  u'recipient': [u'noreply@thousandeyes.com'],
                  u'roundsBeforeTrigger': 1,
                  u'ruleId': 302,
                  u'ruleName': u'Default Transaction Alert Rule'}]}
>>>
```
**Agent List**:

Returns a list of all agents available to your account in ThousandEyes, including both Enterprise and Cloud agents
```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> agent_list = api.agent_list()
>>> pprint(agent_list)
{u'agents': [{u'agentId': 3,
              u'agentName': u'Singapore',
              u'agentType': u'Cloud',
              u'countryId': u'SG',
              u'ipAddresses': [u'202.150.211.165',
                               u'202.150.211.164',
                               u'202.150.211.163',
                               u'202.150.211.171',
                               u'202.150.211.173',
                               u'202.150.211.172',
                               u'202.150.211.168',
                               u'202.150.211.169',
                               u'202.150.211.167',
                               u'202.150.211.176',
                               u'202.150.211.177',
                               u'202.150.211.175'],
              u'location': u'Singapore'},
             {u'agentId': 4,
              u'agentName': u'Tokyo, Japan',
              u'agentType': u'Cloud',
              u'countryId': u'JP',
              u'ipAddresses': [u'106.186.22.219',
                               u'106.186.20.119',
                               u'106.187.53.37',
                               u'106.186.27.94',
                               u'106.186.118.155',
                               u'106.186.120.36',
                               u'106.187.45.142',
                               u'106.187.50.192',
                               u'106.185.26.19',
                               u'106.186.21.160'],
              u'location': u'Tokyo, Japan'},
             {u'agentId': 5,
              u'agentName': u'Atlanta, GA',
              u'agentType': u'Cloud',
              u'countryId': u'US',
              u'ipAddresses': [u'50.116.42.197',
                               u'50.116.39.7',
                               u'173.230.135.107',
                               u'23.92.28.179',
                               u'23.92.30.176',
                               u'50.116.43.195',
                               u'74.207.228.78',
                               u'50.116.32.183',
                               u'198.74.53.226',
                               u'74.207.226.105',
                               u'66.228.60.9',
                               u'173.230.133.163',
                               u'23.92.29.206',
                               u'192.155.93.178',
                               u'198.74.53.88'],
              u'location': u'Atlanta Area'},
             {...},
             {u'agentId': 16769,
              u'agentName': u'Kansas City, MO',
              u'agentType': u'Cloud',
              u'countryId': u'US',
              u'ipAddresses': [u'74.91.16.173',
                               u'74.91.16.171',
                               u'74.91.16.172'],
              u'location': u'Kansas City Area'}]}

```

**Agent Details**:

Returns details for an agent, including assigned tests. Enterprise agents show utilization data and assigned accounts.
```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> agent_details = api.agent_details(16769)
>>> pprint(agent_details)
{u'agents': [{u'agentId': 16769,
              u'agentName': u'Kansas City, MO',
              u'agentType': u'Cloud',
              u'countryId': u'US',
              u'ipAddresses': [u'74.91.16.173',
                               u'74.91.16.171',
                               u'74.91.16.172'],
              u'location': u'Kansas City Area'}]}

```

**Agent Update**:

Updates Enterprise Agent details. Users can update the agent display
name, as well as change test and account assignments.

This endpoint can only be used for Enterprise Agents, and only for
users in a role that permits modification of Enterprise Agents.

Important notes related to agent modification on tests:

- if an agent is removed from a test, the modification date for tests
  using that agent at the time it was removed will be changed.
- If an agent is removed from an entire account, then all tests using
  this agent in the removed account will be updated to reflect the
  removed agent.
- If a removed agent is the final remaining agent on a test, then the
  test will be disabled when the agent is removed.

```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> update_agent = api.update_agent(966, agentName="my cool updated agent name", accounts=315)
>>> pprint(update_agent)
{u'"agents": [
        {
            "agentId": 966,
            "agentName": "ubuntu1404-x64",
            "location": "San Francisco Bay Area",
            "countryId": "US",
            "prefix": "50.128.0.0/9",
            "utilization": 1,
            "ipAddresses": [
                "192.168.1.223"
            ],
            "publicIpAddresses": [
                "50.184.189.59"
            ],
            "enabled": 1,
            "accounts": [
                {
                    "aid": 315,
                    "accountName": "Documentation"
                },
                {
                    "aid": 362,
                    "accountName": "Enterprise Agents Dashboard"
                }
            ],
            "tests": [
                {
                    "createdDate": "2015-02-03 21:55:13",
                    "modifiedDate": "2015-05-14 23:18:03",
                    "createdBy": "API Sandbox User (noreply@thousandeyes.com)",
                    "modifiedBy": "API Sandbox User (noreply@thousandeyes.com)",
                    "enabled": 1,
                    "savedEvent": 0,
                    "testId": 12065,
                    "testName": "My Google DNS test",
                    "type": "dns-server",
                    "interval": 300,
                    "domain": "google.com A",
                    "networkMeasurements": 1,
                    "mtuMeasurements": 1,
                    "bandwidthMeasurements": 0,
                    "bgpMeasurements": 1,
                    "alertsEnabled": 0,
                    "liveShare": 0,
                    "recursiveQueries": 0,
                    "dnsServers": [
                        {
                            "serverId": 130,
                            "serverName": "ns2.google.com."
                        }
                    ],
                    "apiLinks": [...]
                },
                {
                    "enabled": 1,
                    "testId": 817,
                    "savedEvent": 0,
                    "liveShare": 0,
                    "testName": "http://www.thousandeyes.com",
                    "type": "http-server",
                    "interval": 900,
                    "url": "http://www.thousandeyes.com",
                    "networkMeasurements": 1,
                    "createdBy": "API Sandbox User (noreply@thousandeyes.com)",
                    "modifiedBy": "API Sandbox User (noreply@thousandeyes.com)",
                    "createdDate": "2012-06-28 19:33:12",
                    "modifiedDate": "2015-05-14 23:18:03",
                    "apiLinks": [...]
                }
            ],
            "network": "Comcast Cable Communications, Inc. (AS 7922)",
            "agentType": "Enterprise",
            "lastSeen": "2015-05-14 23:18:00",
            "agentState": "Online"
        }
    ]
}  

```
**Delete Agent**:
Deletes an Enterprise Agent from ThousandEyes. Note: this feature can only be used on Enterprise Agents.

Important notes related to agent removal:

if an agent is deleted, the modification date for tests using that agent at the time it was deleted will be changed.
If a deleted agent is the final remaining agent on a test, then the test will be disabled when the agent is removed.
Important note: if an agent is removed, it must be re-initialized to use the same machine again in different context. Virtual Appliances can be updated using the Reset State button in the Advanced tab of the agent management interface. Users running packaged versions of Linux will need to remove

```
/var/lib/te-agent/\*.sqlite
```

in order to reinitialize an agent.


If an agent is successfully deleted, No Content response will be returned, and an empty JSON response will be in the body of the response.

```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
delete_agent = api.delete_agent(966)
```

**BGP Monitor List**:

Returns a list of all BGP monitors available to your account in ThousandEyes, including both public and private feeds.
```
>>> from ThousandEyesPY import ThousandEyesPY
>>> from pprint import pprint
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> api = ThousandEyesPY(username="noreply@thousandeyes.com", >>> password="g351mw5xqhvkmh1vq6zfm51c62wyzib2")
>>> bgp_monitor_list = api.bgp_monitor_list()
>>> pprint(bgp_monitor_list)
{u'bgpMonitors': [{u'ipAddress': u'195.66.224.51',
                   u'monitorId': 205,
                   u'monitorName': u'London-11',
                   u'monitorType': u'Public',
                   u'network': u'Tata Communications (AS 6453)'},
                  {...},
                  {u'ipAddress': u'195.66.224.32',
                   u'monitorId': 60,
                   u'monitorName': u'London-7',
                   u'monitorType': u'Public',
                   u'network': u'Tinet SpA (AS 3257)'}]}

```
