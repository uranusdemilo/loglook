import re

logfile = open('auth.txt', 'r')
count = 0
line = "start"
lineOut = ''
while line:
   line=logfile.readline()
   logParts = line.split(']: ')
   if(len(logParts) > 1):
      rawDate = logParts[0].split();
      hackDate = rawDate[0]
      if(int(rawDate[1])<10):
         hackDate += "-0" + rawDate[1] + "-" + rawDate[2]
      else:
         hackDate += "-" + rawDate[1] + "-" + rawDate[2]
      lineOut = hackDate + ' '
      print hackDate
      hackDate = ''
      ipaddr = re.findall( r'[0-9]+(?:\.[0-9]+){3}', logParts[1])
      if len(ipaddr)>=1:
         print ipaddr[0]
	  
   #  messageParts=logParts[1].split(' ')
   #for i in range (0,len(messageParts)):
   #   if(messageParts[i] == 'from'):
   #      lineOut +=  messageParts[i + 1].replace(':','')
   #     print lineOut
   #   elif(messageParts[i].startswith("rhost=")):
   #      addressParts=messageParts[1].split('=')
   #      print addressParts
   #      #lineOut += addressParts[1]
			
