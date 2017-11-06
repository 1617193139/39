Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: D:\1617193139²é×Ó³Ç\tmp\test1.py =================
>>> zzc=Employee("zzc",'39','161','test1.py)
	     
SyntaxError: EOL while scanning string literal
>>> zzc=Employee("zzc",'39','161',')
	     
SyntaxError: EOL while scanning string literal
>>> zzc=Employee("zzc",'39','161','man')
>>> zzc.name
'zzc'
>>> zzc.gender
'man'
>>> zzc.
SyntaxError: invalid syntax
>>> zzc.canswim
<bound method Employee.canswim of <__main__.Employee instance at 0x01F98288>>
>>> zzc.canswim
<bound method Employee.canswim of <__main__.Employee instance at 0x01F98288>>
>>> zzc.canswim()
can swim
>>> 
