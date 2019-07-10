import pyodbc 
import pandas as pd
import sqlalchemy as sql

#cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                       "Server=server_name;"
 #                       "Database=db_name;"
  #                      "uid=User;pwd=password")

cnxn = pyodbc.connect('driver={SQL Server};'
                      'server=L-156171445\SQLEXPRESS;'
                      'database=CRUDDB;'
                      'trusted_consnection=yes')
cursor = cnxn.cursor()
cursor.execute("Select * from Employee")                     
#df = pd.read_sql_query('select * from table', cnxn)

rows = cursor.fetchall()
for row in rows:
    print(row)