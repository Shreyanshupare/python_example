hostname = 'localhost'
username = 'root'
password = '******'
database = 'bitcoin'

# Simple routine to run a query on a database and print the results:
##def doQuery( conn ) :
##    cur = conn.cursor()
##    
##
##    cur.execute(sql)
##
##    
##        
print("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
##doQuery( myConnection )
myConnection.close()
