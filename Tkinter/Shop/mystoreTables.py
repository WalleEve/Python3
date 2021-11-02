import sqlite3
from sqlite3 import Error
import os
import sys

# SQLITE CONNECTIONS:

class DbConnection:
	def __init__(self, dbname):
		self.dbname = dbname # "mystoredb.db"
		self.base_path = os.path.dirname( os.path.abspath(__file__))
		self.config_path = os.path.join(self.base_path, self.dbname)


	def dbCreation(self):

		try:
			self.conn = sqlite3.connect(self.config_path)
			print(sqlite3.version)
		except Error as e:
			print(e)

	def create_app_tables(self):
		""" create a database connection to a SQLite database """
		conn = None
		try:
			conn = sqlite3.connect(self.config_path)
			cursor = conn.cursor()

			sql = """ CREATE TABLE current_transaction(
			tid INT PRIMARY KEY,
			tdate DATE,
			itme CHAR(30),
			unit INT,
			price INT)
			"""

			cursor.execute(sql)
			print("Table APP_USERS created successfully........")
			# Commit your changes in the database
			conn.commit()
			#Closing the connection
			conn.close()

		except Error as e:
			print(e)
		finally:
			if conn:
				conn.close()




def mainDB(dbname):
	global flag
	flag = False
	base_path = os.path.dirname( os.path.abspath(__file__))
	config_path = os.path.join(base_path, dbname)
	print(base_path)
	print(config_path)
	if os.path.exists(config_path):
		flag = True
	return flag

if __name__ == "__main__":
	dbname = input("Please enter DB Name: ")
	flag = mainDB(dbname)
	if flag:
		print("Db exists")
		dbc = DbConnection(dbname)
		dbc.create_app_tables()
	else:
		print("Db not exists")
		dbc = DbConnection(dbname)
		dbc.dbCreation()
		dbc.create_app_tables()
