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


listOfTables = cur.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='TEACHER'; """).fetchall()

if listOfTables == []:
    print('Table not found!')
else:
    print('Table found!')

# commit changes
con.commit()


current_transaction = """ CREATE TABLE current_transaction(
tid INT PRIMARY KEY,
bill_id INT,
tdate DATE,
itme CHAR(30),
unit INT,
price INT)
"""

cursor.execute(current_transaction)
transaction_history  = """ CREATE TABLE transaction_history(
trans_id int PRIMARY KEY,
bill_id INT
trans_date DATE,
item_id CHAR(30),
unit INT,
price INT

)

"""


inhouse_stock = """CREATE TABLE inhouse_stock(
stock_id INT PRIMARY KEY NOT NULL,
item_id INT NOT NULL,
item_name CHAR(30) NOT NULL,
item_unit CHAR(30) CHECK(item_unit in ('KG', 'LT', 'GM', 'ML', 'QT', 'TN', 'PIC', 'PACK', 'BTL')),
unit_price INT NOT NULL,
total_pur_quantity INT, NOT NULL
purchase_date DATE NOT NULL,
total_sale_quantity INT NOT NULL
)
"""

item_master = """CREATE TABLE item_master(
item_id INT PRIMARY KEY,
item_name CHAR(30) ,
item_brand CHAR(30),
UNIQUE(item_name, item_brand)


)
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
