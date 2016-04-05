# coding=utf-8
import urllib
import urllib2
import platform

url = 'http://127.0.0.1:8080/api/v1/game/check_in'
values = {
    'game_name': 'Test Güame',
    'game_status': 'pre-alpha',
    'game_website': 'http://blah.com',
    'listing_contact': 'blah@blah.com',

    'telnet_hostname': 'blah.com',
    'telnet_port': '1234',
    'web_client_url': 'http://webclient.blah.com',

    'connected_player_count': 10,
    'total_player_count': 123,

    'evennia_version': '0.5.0',
    'python_version': platform.python_version(),
    'django_version': '1.8.x',
    'server_platform': platform.platform(),
}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
try:
    response = urllib2.urlopen(req)
except urllib2.HTTPError as exc:
    print exc.read()
else:
    result = response.read()
    print result
