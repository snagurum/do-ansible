import os
import psycopg2

#DB_NAME = os.environ['DB_NAME']
#DB_USER = os.environ['DB_USER']
#DB_PASS = os.environ['DB_PASS']
#DB_HOST = os.environ['DB_HOST']

DB_NAME = 'hello'
DB_USER = 'hello'
DB_PASS = 'hello'
#DB_HOST = '10.104.0.4'
DB_HOST = '188.166.237.86'
# above should be changed to private, easier for testing from local with public ip

DB_PORT = "5432"

def getHello():
   print("starting getHello-function")
   conn = psycopg2.connect(database=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT)
   print("Database connected successfully")

   cur = conn.cursor()
   cur.execute("SELECT * FROM hello")
   rows = cur.fetchall()
   temp = ""
   for data in rows:
      temp = temp +', '+ str(data[0])

   print('Data fetched successfully and shown on the terminal!')
   conn.close()
   return temp

print("starting dbHello.py")
getHello()
