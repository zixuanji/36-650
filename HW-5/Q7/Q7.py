import subprocess
import sys

import psycopg2 ## already installed & can import it directly

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

cur.execute("insert into employee(id, fname, lname) VALUES (generate_series(1, 500), substr(MD5(random()::text), 0, 11), substr(MD5(random()::text), 0,11)) ");

cur.execute("SELECT * from employee");

rows = cur.fetchall()
for row in rows:
    print (row)

conn.commit()
conn.close()
