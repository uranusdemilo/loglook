import re
import sys

logfile = open('maillog.txt','r')
line = 'start'
while line:
   line=logfile.readline()
   lineParts=line.split()
   partPart=lineParts[4].split('/')
   agentName=partPart[1].split('[')
   if agentName[0]=='smtpd' and lineParts[5]=='connect':
	ipAddr = re.findall( r'[0-9]+(?:\.[0-9]+){3}',line)
	if len(ipAddr)>=1:
		print ipAddr[0]
