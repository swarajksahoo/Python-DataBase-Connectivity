import pyodbc
import pandas as pd
import pandas.io.sql

conn = pyodbc.connect("DSN=Hivedsn", autocommit=True, configuration={''job-queue-name' : 'Que-name-assign-to-you'})

#extracting sample 100 rows
df = pandas.io.sql.read_sql("Select * from table_name limit 100")

pandas.io.sql.execute("Creating table table_name2 as Select * from table_name")
