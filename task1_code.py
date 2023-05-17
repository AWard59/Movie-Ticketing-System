import re
from settings import mysql_connection


## write a function to check if a number has string or  not
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

# write a function for for validating an Email
def check_email(email):
    # pass the regular expression and the string into the fullmatch() method
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.fullmatch(pattern, email):
    #return Boolean Value
      return True
    else:
      return False

## form to validate
def register(registration_form):
    name = registration_form['name']
    email = registration_form['email']
    username = registration_form['username']
    # name length should be greater than 3 and should not have any digits
    if len(name) <= 3 or has_numbers(name):
        return "the name should have a minimum length of 4 characters and must not contain any digits."
    # username should have a minimum length of 5 characters
    if len(username) < 5:
        return "the username must have a minimum length of 5 characters."
    ## check email validation here
    if not check_email(email):
        return "Invalid email."
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
