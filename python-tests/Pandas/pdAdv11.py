#Pandas sql operation
import pandas as pd
import sqlite3

#create sql table
create_table = """
CREATE TABLE student_score
(Id INTEGER,Name VARCHAR(20),Math REAL,Science REAL);"""

#execute sql statement
executeSQL = sqlite3.connect('memory')
executeSQL.execute(create_table)
executeSQL.commit()

#prepare  a sql query
SQL_query = executeSQL.execute('select * from student_score')

#fetch result from SQLite database
resultset = SQL_query.fetchall()

#view result
print(resultset)
