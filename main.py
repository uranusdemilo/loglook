import re
import sqlite3

def periodsToUnderscores(ipaddress):
   tableName='ip_' + ipaddress.replace('.','_')
   return tableName
   
con = sqlite3.connect('intruders')
cur = con.cursor()
logfile = open('auth.txt', 'r')
count = 0
line = "start"
lineOut = ''
intruders = []
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
      ipaddr = re.findall( r'[0-9]+(?:\.[0-9]+){3}', logParts[1])
      if len(ipaddr)>=1:
         tableName=periodsToUnderscores(ipaddr[0])
         isThereQuery = 'SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'' + tableName + '\''
         isThere=cur.execute(isThereQuery)
         isTable=isThere.fetchone()
         if(isTable == None):
            isTable = isThere.fetchone()    
            makeTableCommand='create table ' + tableName + '(hacker char(15), hackDate char(15))'
            sqlCommand=sqlCommand='insert into ' + tableName + ' values(\'' + ipaddr[0] +  '\',\'' + hackDate + '\')'
            cur.execute(makeTableCommand)
            cur.execute(sqlCommand)
            intruders.append(tableName)            
         else:
            sqlCommand='insert into ' + tableName + ' values(\'' + ipaddr[0] +  '\',\'' + hackDate + '\')'
            cur.execute(sqlCommand)
for g in range(len(intruders)):
   countSqlCommand='select count(*) from ' + intruders[g]
   numAttackQuery=cur.execute(countSqlCommand);
   numAttacks=numAttackQuery.fetchone()
   print intruders[g] + '  number of attacks = ' + str(numAttacks[0])
            
