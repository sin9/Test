#coding=utf-8
import urllib
import urllib.request
data2 = {}
data2['word'] = 'sin'
url_value = urllib.parse.urlencode(data2)
print(url_value)
url="http://valaire.mu/"
full_url=url+url_value
print(full_url)
data=urllib.request.urlopen(url).read()
data=data.decode('UTF-8')
print(data)

