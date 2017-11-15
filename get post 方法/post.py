import urllib2

volues={}
values['username'] = "1165316948@qq.com"
values['password'] = 'xuelei123'
date = urllib.urlencode(values)
url = "http://passport.cadn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Requesl(url,data)
response = urllib2.urlopen(request)
print response.read()
