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
    # create connection
    mydb = mysql_connection()
    sql = mydb.cursor()
    try:
        name = registration_form['name']
        email = registration_form['email']
        username = registration_form['username']
        password = registration_form['password']
        date = registration_form['dob']
        # name length should be greater than 3 and should not have any digits
        if len(name) <= 3 or has_numbers(name):
            raise ValueError(
                "the name should have a minimum length of 4 characters and must not contain any digits.")
        ## check if username already in database, use 'where' clause
        sql.execute("SELECT * FROM my_users WHERE username = %s", (username,))
        existing_username = sql.fetchone()
        if existing_username:
            raise ValueError("username already taken, try another username.")
        # username should have a minimum length of 5 characters
        if len(username) < 5:
            raise ValueError(
                "the username must have a minimum length of 5 characters.")
        ## check email validation here
        if not check_email(email):
            raise ValueError("Invalid email.")
        ## password should be greater than 8 digits and must have numbers, reuse has_number function
        if len(password) <= 8 or not has_numbers(password):
            raise ValueError(
                "password should be greater than 8 digits and must have numbers.")
        # if all validations pass, create a new record, insert values into table
        sql.execute("INSERT INTO my_users (name, username, email, date, password) VALUES (%s, %s, %s, %s, %s)",
                    (name, username, email, date, password))
        mydb.commit()
    except ValueError as error:
        return str(error)
    return 'successfully registered'


def capture_data(registration_form):
    # Create the my_users table if it doesn't exist
    mydb = mysql_connection()
    sql = mydb.cursor()
    sql.execute("""
            CREATE TABLE IF NOT EXISTS my_users (
            name varchar(255) DEFAULT NULL,
            USERNAME varchar(255) DEFAULT NULL,
            email varchar(255) DEFAULT NULL,
            date varchar(255) DEFAULT NULL,
            password varchar(255) DEFAULT NULL
            )
        """)
    mydb.commit()

    result = register(registration_form)
    ## if registration is valid
    if result:
        return result

    # Check for database entries
    sql.execute("SELECT COUNT(*) FROM my_users")
    count = sql.fetchone()[0]
    if count == 1:
        return 'single entry'
    elif count > 1:
        return 'multiple entries'
    else:
        return 'no entries'

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
