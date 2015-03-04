import re
str1='this is an long buch of text with address=192.168.1.223 embedded'
ipaddr = re.findall( r'[0-9]+(?:\.[0-9]+){3}',str1 )
print ipaddr

