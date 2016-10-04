import re
import sys

logfile = open('maillog.txt','r')
line = 'start'
while line:
   line=logfile.readline()
   lineParts=line.split()
   partPart=lineParts[4].split('/')
   agentName=partPart[1].split('[')
   if agentName[0]=='smtpd':
	print lineParts[5:]

