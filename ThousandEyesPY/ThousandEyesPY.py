import requests
import json

class ThousandEyesPY(object):
    """docstring for ThousandEyesAPI"""
    def __init__(self, USERNAME, PASSWORD):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD

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
        if not isinstance(id, int) and aid is not None:
            raise ValueError('Required Integer or None')
        return str(id)
    def active_alerts(self, window_integer=None, window_unit=None, output_format='json', aid=None):
        """
        Access all current alerts for time filter provided, if no time filter
        is provided it will return all active alerts.
        """
        window = self._generate_window(window_integer=window_integer, window_unit=window_unit)

        output_format = self._format_validation(output_format=output_format)

        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'window': window,
                        'aid:': aid
                  }
        print self.USERNAME, self.PASSWORD
        r = requests.get(self.THOUSANDEYES_API_URL() + 'alerts', auth=(self.USERNAME, self.PASSWORD), params=payload)
        # Use requests built in Raise for Status of 400
        r.raise_for_status()
        
        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j

    def active_alert_detail(self, alert_id=None, output_format='json', aid=None):
        """
        Recieve the details of a specific Active Alert
        """
        alert_id = self._id_validation(id=alert_id)

        output_format = self._format_validation(output_format=output_format)

        aid = self._aid_validation(aid=aid)

        payload = {
                        'format': output_format,
                        'aid:': aid
                  }

        r = requests.get(self.THOUSANDEYES_API_URL() + 'alerts/' + alert_id, auth=(self.USERNAME, self.PASSWORD), params=payload)
        # Use requests built in Raise for Status of 400
        r.raise_for_status()

        j = json.loads(r.text)
        # print json.dumps(j, indent=4)
        return j
