import sqlite3
from sqlite3 import Error
import os
import sys
from datetime import date


base_path = os.path.dirname( os.path.abspath(__file__))
config_path = os.path.join(base_path, 'mystoredb.db')

conn = sqlite3.connect(config_path)
print(sqlite3.version)
cursor = conn.cursor()

sql = """ CREATE TABLE current_transaction(
tid INT PRIMARY KEY,
tdate DATE,
itme CHAR(30),
unit INT,
price INT)
"""

#cursor.execute(sql)
print("Table current_transaction created successfully........")

sql  = """
insert into current_transaction values(?,?,?,?,?)
"""
#cursor.execute(sql, (1+1, date.today(), 'rice', 5, 450))

sql = "select * from current_transaction"
cursor.execute(sql)
for i in cursor.fetchall():
    print(i)
conn.commit()
#Closing the connection
conn.close()
