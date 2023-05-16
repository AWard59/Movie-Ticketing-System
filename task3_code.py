import re
from settings import mysql_connection


mydb = mysql_connection()
## create cursor
sql = mydb.cursor()
#select ticket and ids


def select_movie(movie_id, no_of_tickets):

    ##take movie id and no of tickets as inputs

    ## only 5 tickets for a person condition validation

    ##select movie_id and avaibility from the database

    ##validate if a particular movie id is available

    ## Display how many tickets available

    ## assume that payment gateway has processed (at the counter)

    #update the tickets dynamically into database (Change the type to int) (tickets available - ticket booked)

    ## this is to maintain realistic records

    ## write update query, change from int to string record where movie_id = 'value'

    #return True when success
    #default return should be False
    return False

    ##challenge since the ticket count is in varchar format in table, you have to dynamically convert type and validate


#do not delete following function
def task_runner():
    print(select_movie(1001, 2))
