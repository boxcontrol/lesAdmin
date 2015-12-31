import requests


def sQuery(url, api_hash, api_key, values, action):


    values.update({'rdtype': 'json', 'hash': api_hash, 'key': api_key, 'action': action})
    response = requests.get('https://'+url+'/api/client/command.php', params=values, timeout=50)
    return response.text


def sQuery1(url, api_hash, api_key, extra=''):

    response = requests.get('https://'+url+'/api/client/command.php?key='
                            + api_key + "&hash=" + api_hash
                            + "&action=info&"
                            + extra, timeout=50)
    return response.text


class myServer:
    def __init__(self, url, api_hash, api_key):
        self.url = url
        self.api_hash = api_hash
        self.api_key = api_key
        self.values = ({'rdtype': 'json', 'hash': self.api_hash, 'key': self.api_key})

    def get_status(self):
        return sQuery(self.url, self.api_hash, self.api_key, self.values, action='status')

    def get_info(self):
        return sQuery(self.url, self.api_hash, self.api_key, self.values, action='info')

    def get_full_info(self):
        extra = 'ipaddr=true&hdd=true&mem=true&bw=true'
        return sQuery1(self.url, self.api_hash, self.api_key, extra=extra)

    def server_reboot(self):
        return sQuery(self.url, self.api_hash, self.api_key, self.values, action='reboot')

    def server_shutdown(self):
        return sQuery(self.url, self.api_hash, self.api_key, self.values, action='shutdown')

    def server_boot(self):
        return sQuery(self.url, self.api_hash, self.api_key, self.values, action='boot')
