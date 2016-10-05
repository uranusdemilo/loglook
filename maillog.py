import re
import sys

logfile = open('maillog.txt','r')
outfile = open('out.txt','w')
line = 'start'
ipsAll=[]
ipsEach=[]
lineCount=0;
matchCount = 0;
smtpdCount = 0;
while line:
	line=logfile.readline()
	lineParts=line.split();
	if len(lineParts) > 5 and lineParts[5] == 'connect':
		ipdata = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line)
		ipaddr=ipdata[0]
		ipsAll.append(ipaddr)
		if ipaddr not in ipsEach:
			ipsEach.append(ipaddr)
for ipe in ipsEach:
	for ipa in ipsAll:
		if ipe == ipa:
			matchCount += 1
	if matchCount > 4:
		print "%s %d" %(ipe,matchCount)
	matchCount = 0
				

		
		