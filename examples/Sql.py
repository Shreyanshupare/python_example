#!/usr/bin/python

hostname = 'localhost'
username = 'root'
password = 'bizruntime@123'
database = 'bitcoin'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS EMPL")
    sql = """CREATE TABLE EMPL (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

    cur.execute(sql)

    
        
print("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

# Simple routine to run a query on a database and print the results:

        

