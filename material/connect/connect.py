import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=db_name;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
