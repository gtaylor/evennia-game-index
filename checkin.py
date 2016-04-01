import urllib
import urllib2

url = 'http://127.0.0.1:8080/api/v1/game/check_in'
values = {
    'game_name': 'Test Game',
    'game_status': 'pre-alpha',
    'game_website': 'http://blah.com',
    'telnet_hostname': 'blah.blah.com',
    'telnet_port': '1234',
    'connected_player_count': 123,
}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
result = response.read()
print result
