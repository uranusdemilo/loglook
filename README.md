Loglook is a python script that analyzes log the authentication log (/var/log/auth.log) files sorting the number of log entries by the IP address of the person connecting to the server.  It was created to identify the most brazen and persistent SSH hackers that were attempting to break into my network.  

To implement Loglook, you will need to install Python and SQLite3.  You will also need to create a blank SQLite3 database with the name of "intruders".  You will also need to copy the servers log file to the directory from where Loglook runs, and to grant yourself read rights to it.  

Loglook works by reading the auth.log file line-by-line, and picking out IP addresses.  When it finds an IP address it hasn't recorded yet, it places that address in an array, and creates a table with the name of iP_xxx_xxx_xxx_xxx, where the x's and underscores count as the numbers in the IP address.  Next, pushes the table name into an array, then makes a database entry with pertinent information into this table.  On subsequent reads, the script checks the contents of the table-name array when it finds and address....it creates a table only when it finds an IP address that is not in the array.  If it finds the table name in the array, it skips the table creations process and merely updates the table.

Output looks something line this:

ip_1_215_253_186    number of attacks =  2306   1.215.253.186
ip_222_216_29_175   number of attacks =   108   222.216.29.175
ip_82_102_180_11    number of attacks =   484   82.102.180.11
ip_61_240_144_64    number of attacks =     1   61.240.144.64
ip_162_239_210_138  number of attacks =    28   162.239.210.138
ip_182_100_67_115   number of attacks =   276   182.100.67.115
ip_192_3_170_208    number of attacks =    65   192.3.170.208

The first column is handy for copy-and-pasting table names into SQL statements.  The 2nd column indicates the number of log entries (note, not reall the number of attacks....I'm working on that one) for the given IP address.  The last column indicates the IP adress from which the table name was derived.  It's handy for copy-and-pasting into websites like www.abuseipdb.com for a quick identification of where the attack is originating from....and if anyone else has had issues with it.

Development is ongoing...
