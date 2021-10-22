import subprocess
import sys

import psycopg2 ##already installed & can import it directly

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

cur.execute("SELECT * from employee limit 10");

rows = cur.fetchall()
for row in rows:
    print (row)
    
conn.commit()
conn.close()