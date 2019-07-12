import pyodbc 
import pandas as pd
import sqlalchemy as sql

#cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                       "Server=server_name;"
 #                       "Database=db_name;"
  #                      "uid=User;pwd=password")

cnxn = pyodbc.connect('driver={SQL Server};''server=L-156171445\SQLEXPRESS;''database=CRUDDB;''trusted_consnection=yes')
cursor = cnxn.cursor()
cursor.execute("""Select count(*) from Employee

""") 
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""Insert into Employee Values('Navya11', 'ProjectEngineer1', 241, 500001)

""") 
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


cursor.execute("""Select count(*) from Employee

""")   
                  
#df = pd.read_sql_query('select * from table', cnxn)

rows = cursor.fetchall()
for row in rows:
    print(row)