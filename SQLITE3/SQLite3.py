
# IMPORTS MODULES
from sqlite3 import *
from sqlite3 import Error as e
import os as os
import sys

class MySqlite3:
     """
     This class contains all the sqlite3 functionarly liek CRUD for application
     """
     def __init__(self, dbname):
         self.base_path = os.path.dirname( os.path.abspath(__file__))
         self.config_path = os.path.join(base_path, dbname)

     def dbCreation(self):
        conn = None
        try:
            conn = sqlite3.connect(self.config_path)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

     def tableCreation(self, sql):
         conn = None
         try:
             conn = sqlite3.connect(self.config_path)
             print(sqlite3.version)
             cursor = conn.cursor()
             cursor.execute(sql)
         except Error as e:
             print(e)
         finally:
             if conn:
                 conn.close()

     def crud_execute(self, sql):

         conn = None
         try:
             conn = sqlite3.connect(self.config_path)
             print(sqlite3.version)
             cursor = conn.cursor()
             cursor.execute(sql)
             conn.commit()
         except Error as e:
             print(e)
         finally:
             if conn:
                 conn.close()
