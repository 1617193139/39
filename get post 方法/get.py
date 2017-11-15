import urllib2

volues={}
values['username'] = "1165316948@qq.com"
values['password'] = 'xuelei123'
date = urllib.urlencode(values)
url = "http://passport.cadn.net/account/login"
geturl = url + "?"+data
request = urllib2.Requesl(gelurl)
response = urllib2.urlopen(request)
print response.read()
