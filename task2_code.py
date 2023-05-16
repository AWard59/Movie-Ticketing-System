import re
from settings import mysql_connection

##REference link for mysql with python (for students)
#https://www.w3schools.com/python/python_mysql_getstarted.asp


mydb = mysql_connection()
## create cursor
sql = mydb.cursor()

#Task 2


def display_shows():

    ##dynamically fetch shows from movie table and display
    #the name of the table is movies
    #use sql to fetch shows by selecting movie_name, show_time, date
    return_dict = {}
    my_list = []

    ##write your code here

    return_dict['show'] = my_list
    #result list of dict with keys  'movie_id', 'movie', 'show_time', 'date'
    return return_dict

#verify the return string


#do not delete following function
def task_runner():
    print(str(display_shows()))
