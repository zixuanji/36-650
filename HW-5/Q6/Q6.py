import subprocess
import sys

import psycopg2 ##already installed in terminal & can import it directly

#tweak the database parameters to match your specific postgres database.
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="Jin981128", 
                        database="postgres"
                        #You may add the following line if you have schemaa
                        #,options="-c search_path=nfl"
                       )
cur = conn.cursor()


table = "create table employee (id SERIAL, fname VARCHAR(10), lname VARCHAR(10));"

cur.execute(table)

conn.commit()

conn.close()
