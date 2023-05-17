import mysql.connector


#Following function will create a mysql connection.
def mysql_connection():
    #Get your DB connection from "DataBase Info" Tab
    HOST = 'localhost'
    USERNAME = 'bc71c215'
    PASSWORD = 'Cab#22se'
    DATABASE = 'bc71c215'

    mydb = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )
    ## returns cursor
    sql = mydb.cursor()

    sql.execute("""
          CREATE TABLE IF NOT EXISTS my_users (
          name varchar(255) DEFAULT NULL,
          username varchar(255) DEFAULT NULL,
          email varchar(255) DEFAULT NULL,
          date varchar(255) DEFAULT NULL,
          password varchar(255) DEFAULT NULL
          )
        """)
    
    return mydb
