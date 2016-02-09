import requests
import json
from decorators import handleError


class ThousandEyesPY(object):
    """docstring for ThousandEyesAPI"""
    def __init__(self, username=None, password=None):
        if (username and not password) or (not username and password):
            raise ValueError('Must provide username and password for ThousandEyes Service')
        elif not username and not password:
            raise ValueError('Must provide username and password for ThousandEyes Service')
        else:
            self.username = username
            self.password = password

    def THOUSANDEYES_API_URL(self):
        """ Returns current THOUSANDEYES_API_URL"""
        return "https://api.thousandeyes.com/"

    def _generate_window(self, window_integer=None, window_unit= None):
        """
        window=[0-9]+[smhdw]? specifies a window of time for the result set.
        """
        if not isinstance(window_integer, int) and window_integer is not None:
            raise ValueError('Required Integer or None')

        # window_unit = 's', 'm', 'h', 'd', 'w'
        # Stands for second, minute, hour, day, week
        window_format_list = ['s', 'm', 'h', 'd', 'w']
        if window_unit not in window_format_list and window_unit is not None:
            raise ValueError('Incorrect must be "s", "m", "h", "d", "w", or None')

        # Both window_integer and window_unit must be provided if using these paramaters
        if (window_integer and not window_unit) or (not window_integer and window_unit):
            raise ValueError('Must provide both window unit and window integer or neither')
        elif not window_integer and not window_unit:
            window = None
        else:
            window = "{}{}".format(window_integer, window_unit)

        return window

    def _format_validation(self, output_format="json"):
        """
        format=json|xml optional, specifies the format of output requested
        """
        format_list = ['json', 'xml']
        if output_format not in format_list:
            raise ValueError('Output Format must be set to "json" or "xml", default is "json"')
        return output_format

    def _aid_validation(self, aid=None):
        """
        aid=x optional, changes the account group context of the current user.
        # If an invalid account ID is specified as a parameter, the response
        # will come back as an HTTP/400 error
        """
        if not isinstance(aid, int) and aid is not None:
            raise ValueError('Required Integer or None')
        return aid

    def _id_validation(self, id=None):
        """
        id is required to be a integer.
        """
        if not isinstance(id, int) and id is not None:
            raise ValueError('Required Integer or None')
        return str(id)

    def active_alerts(self, window_integer=None, window_unit=None, aid=None):
        """
        Access all current alerts for time filter provided, if no time filter
        is provided it will return all active alerts.
        """
        window = self._generate_window(window_integer=window_integer, window_unit=window_unit)
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'window': window,
                        'aid:': aid
                  }

        r = requests.get(self.THOUSANDEYES_API_URL() + 'alerts', auth=(self.username, self.password), params=payload)
        # Use requests built in Raise for Status of 400
        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    def active_alert_detail(self, alert_id=None, aid=None):
        """
        Recieve the details of a specific Active Alert
        """
        alert_id = self._id_validation(id=alert_id)
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'aid:': aid
                  }

        r = requests.get(self.THOUSANDEYES_API_URL() + 'alerts/' + alert_id, auth=(self.username, self.password), params=payload)
        # Use requests built in Raise for Status of 400
        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    @handleError
    def alert_rules(self, aid=None):
        """
        Recieve the details of a specific Active Alert
        """
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'aid:': aid
                  }

        r = requests.get(self.THOUSANDEYES_API_URL() + 'alert-rules', auth=(self.username, self.password), params=payload)
        # Use requests built in Raise for Status of 400

        r.raise_for_status()


        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    def agent_list(self, aid=None):
        """
        Returns a list of all agents available to your account in ThousandEyes,
        including both Enterprise and Cloud agents.

        Response:

        Sends back a Dictionary of agents, specifying agentId, which can be
        used by other areas of the API. The agent's public IP addresses will be
        shown, along with last. If an agent is an Enterprise agent, the agent's
        public and private IP addresses will be shown, as well as the public
        network in which the agent is located.
        Return Fields:

        Field -- Data Type -- Units -- Notes
        agentId -- integer -- n/a -- unique ID of agent
        agentName -- string -- n/a -- display name of the agent
        agentType -- string -- n/a -- Cloud, Enterprise or Enterprise Cluster, shows the type of agent
        countryId -- string -- n/a -- ISO-3166-1 alpha-2 country code of the agent
        clusterMembers -- array -- n/a -- if an enterprise agent is clustered, detailed information about each cluster member will be shown as array entries in the clusterMembers field. This field is not shown for Enterprise Agents in standalone mode, or for Cloud Agents.
        ipAddresses -- array -- n/a -- array of ipAddress entries
        location -- string -- n/a -- location of the agent
        prefix -- string -- n/a -- Network prefix, expressed in CIDR format (Enterprise Agents only)
        enabled -- boolean -- n/a -- 1 for enabled, 0 for disabled (Enterprise Agents only)
        network -- string -- n/a -- name of the autonomous system in which the Agent is found (Enterprise Agents only)
        lastSeen -- dateTime -- n/a -- yyyy-MM-dd hh:mm:ss, expressed in UTC (Enterprise Agents only)
        agentState -- string -- n/a -- either Online or Offline (standalone Enterprise Agents only)
        verifySslCertificates -- boolean -- n/a -- 1 for enabled, 0 for disabled (Enterprise Agents only)
        keepBrowserCache -- boolean -- n/a -- 1 for enabled, 0 for disabled (Enterprise Agents only)
        """
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'aid:': aid
                  }

        r = requests.get(self.THOUSANDEYES_API_URL() + 'agents', auth=(self.username, self.password), params=payload)
        # Use requests built in Raise for Status of 400
        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    def agent_details(self, agent_id, aid=None):
        """
        Returns details for an agent, including assigned tests. Enterprise
        agents show utilization data and assigned accounts.

        Response:

        Sends back agent details for an agent. For Enterprise Agents,
        additional details, including a list of accounts to which the agent is
        assigned, and utilization details will be shown. Metadata is shown
        below:

        Field -- Data Type -- Units -- Notes
        agentId -- integer -- n/a -- unique ID of agent
        agentName -- string -- n/a -- display name of the agent
        location -- string -- n/a -- location of the agent
        countryId -- string -- n/a -- ISO-3166-1 alpha-2 country code of the agent
        prefix -- string -- n/a -- Network prefix, expressed in CIDR format
        utilization -- integer -- percentage -- shows overall utilization percentage
        ipAddresses -- array -- n/a -- array of ipAddress entries
        enabled -- boolean -- n/a -- 1 for enabled, 0 for disabled
        accounts -- array -- n/a -- list of accounts to which the agent is assigned, showing aid and accountName fields
        tests -- array -- n/a -- list of tests assigned to the agent, expressed in the same format as /tests endpoint
        network -- string -- n/a -- name of the autonomous system in which the Agent is found
        agentType -- string -- n/a -- either Cloud, Enterprise, or Enterprise Cluster, shows the type of agent
        lastSeen -- dateTime -- n/a -- yyyy-MM-dd hh:mm:ss, expressed in UTC
        agentState -- string -- n/a -- either Online or Offline
        """
        agent_id = self._id_validation(id=agent_id)
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'aid:': aid
                  }

        r = requests.get(self.THOUSANDEYES_API_URL() + 'agents/' + agent_id, auth=(self.username, self.password), params=payload)
        # Use requests built in Raise for Status of 400
        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    def update_agent(self, agent_id, aid=None, agentName=None, accounts=None, tests=None):
        """

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

        Post Data

        When POSTing data to the
        /agents/{agentId}/update
        endpoint, users can update the following fields:

        - 'agentName' string representation of an agent. No two agents can have
          the same display name.
        - 'accounts' an array of account objects containing only an aid value,
          in the format { aid: integer }. See /accounts to pull a list of
          account IDs - a list of dictionaries can be accepted: [{"aid": 315},
          {"aid": 362}]
        - 'tests' an array of test objects containing only a testId value in
          the format { testId: integer }. See /tests to pull a list of tests
          available in the current account context. A list of dictionaries can
          be accepted: [{"testId": 12065}, {"testId": 817}]

        Response

        If an agent is successfully edited, an HTTP/200 OK response will be
        returned, and the agent's assigned accounts / tests will change; the
        newly updated agent data will be returned. See the example below:

        Field -- Data Type -- Units -- Notes
        agentId -- integer -- n/a -- unique ID of agent
        agentName -- string -- n/a -- display name of the agent
        location -- string -- n/a -- location of the agent
        countryId -- string -- n/a -- ISO-3166-1 alpha-2 country code of the agent
        prefix -- string -- n/a -- Network prefix, expressed in CIDR format
        utilization -- float -- percentage -- utilization of the agent, expressed in decimal format, where 0 = 0% and 1 = 100% utilization
        ipAddresses -- array -- n/a -- array of ipAddress entries
        enabled -- boolean -- n/a -- 1 for enabled, 0 for disabled
        accounts -- array -- n/a -- list of accounts to which the agent is assigned, expressed in the same format as /accounts endpoint
        tests -- array -- n/a -- list of tests assigned to the agent, expressed in the same format as /tests endpoint
        network -- string -- n/a -- name of the autonomous system in which the Agent is found
        agentType -- string -- n/a -- either Cloud or Enterprise, shows the type of agent
        lastSeen -- dateTime -- n/a -- yyyy-MM-dd hh:mm:ss, expressed in UTC
        agentState -- string -- n/a -- either Online or Offline
        """
        agent_id = self._id_validation(id=agent_id)
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'aid': aid,
                        'agentName': agentName,
                        'accounts': accounts,
                        'tests': tests
                  }

        r = requests.post(self.THOUSANDEYES_API_URL() + 'agents/' + agent_id + '/update', auth=(self.username, self.password), json=json.dumps(payload))
        # Use requests built in Raise for Status of 400

        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    def delete_agent(self, agent_id, aid=None):
        """
        Deletes an Enterprise Agent from ThousandEyes. Note: this feature can
        only be used on Enterprise Agents.

        Important notes related to agent removal:

        -  if an agent is deleted, the modification date for tests using that
           agent  at the time it was deleted will be changed.
        -  If a deleted agent is the final remaining agent on a test, then the
           the test will be disabled when the agent is removed.


        Important note: if an agent is removed, it must be re-initialized to
        use the same machine again in different context. Virtual Appliances can be
        updated using the Reset State button in the Advanced tab of the agent
        management interface. Users running packaged versions of Linux will need to
        remove:

        ```/var/lib/te-agent/\*.sqlite```

        in order to reinitialize an agent.

        Request

        {agentId} corresponds the unique ID of an enterprise agent, obtained
        from the /agents endpoint

        Post Data

        When POSTing data to the /agents/{agentId}/delete endpoint, users
        should specify an empty POST body.

        Response

        If an agent is successfully deleted, an HTTP/204 No Content response
        will be returned, and an empty JSON response will be in the body of the
        response.
        """
        agent_id = self._id_validation(id=agent_id)
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                  }

        r = requests.post(self.THOUSANDEYES_API_URL() + 'agents/' + agent_id + '/delete', auth=(self.username, self.password), json=json.dumps(payload))
        # Use requests built in Raise for Status of 400

        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    def bgp_monitor_list(self, aid=None):
        """
        Returns a list of all BGP monitors available to your account in
        ThousandEyes, including both public and private feeds.

        Specifying this parameter without the user to be assigned to the target
        account will result in an error response. See Account Context for more
        information

        Response

        Sends back a collection of BGP monitors, including monitorId, which can
        be used by other areas of the API. The example below shows both a
        public and private BGP monitor.

        Field -- Data Type -- Units -- Notes
        monitorId -- integer -- n/a -- unique ID of BGP monitor
        ipAddress -- string -- n/a -- IP address of the BGP monitor
        network -- string -- n/a -- name of the autonomous system in which the monitor is found
        monitorType -- string -- n/a -- either Public or Private, shows the type of monitor
        monitorName -- string -- n/a -- display name of the BGP monitor
        """
        output_format = self._format_validation()
        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'aid:': aid
                  }

        r = requests.get(self.THOUSANDEYES_API_URL() + 'bgp-monitors', auth=(self.username, self.password), params=payload)
        # Use requests built in Raise for Status of 400
        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j
