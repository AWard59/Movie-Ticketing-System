import re
from settings import mysql_connection


## write a function to check if a number has string or  not
def has_numbers(inputString):
    return None

# write a function for for validating an Email


def check_email(email):

    # pass the regular expression
    # and the string into the fullmatch() method

    #return Boolean Value
    return False


## form to validate
def register(registration_form):

    #your input from your input string (assume from front end , json)

    #name lenth should be greater than 3 and should not have any digits
    ## check email validation here
    ## password should be greater than 8 digits and must have numbers, reuse has_number function
    ## after validation insert into database
    ## create connection
    pass


def capture_data(registration_form):

    ## if registration is valid
    data = register(registration_form)
    if data == True:

        name = registration_form['name']
        email = registration_form['email']
        username = registration_form['username']
        date = registration_form['dob']
        password = registration_form['password']

        ## connect with database
        mydb = mysql_connection()
        ## returns cursor
        sql = mydb.cursor()

        ## check if username already in database, use 'where' clause
        ## if

        #if username not taken create a new record, insert values into table
    else:
        return data


#do not delete following function
def task_runner():
    ## Test data
    name = 'test username'
    user_name = 'testusername'
    email_value = 'test@testgmail.com'
    date_value = '15-12-1999'
    password_value = 'testdfs77ds'
    registration_form = {'name': name,  'username': user_name,
                         'email': email_value, 'dob': date_value, 'password': password_value}
    print(capture_data(registration_form))
