import re
import sqlite3
import sys

def periodsToUnderscores(ipaddress):
   tableName='ip_' + ipaddress.replace('.','_')
   return tableName

def createAddress(tableName):
   tableName=tableName.replace('ip_','')
   tableName=tableName.replace('_','.')
   return tableName
   
def makeSpaces(num,max):
   sp = max - num
   if sp != 0:
      for i in range(0,sp):
         sys.stdout.write(' ')
   else:
      sys.stdout.write('')
   
   
con = sqlite3.connect('intruders')
cur = con.cursor()
logfile = open('auth.log', 'r')
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
   print intruders[g],
   makeSpaces(len(intruders[g]),18)
   print '  number of attacks = ',
   makeSpaces(len(str(numAttacks[0])),5)
   print numAttacks[0],
   print ' ',
   print createAddress(intruders[g])

