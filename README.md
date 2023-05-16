You will be creating a movie ticket reservation system from the ground up. This is a software project that requires logical thinking and programming skills to understand the needs of a booking platform. You will need to take into account various resources, such as theatres, movies, seats, and pricing, and consider the user's experience while dynamically managing the backend. Your input and output objects should resemble JSON, and your logic should be functional and aligned with the test cases provided.

Module 1
In this module, you need to write a backend script that takes the registration details and stores it in a database. You need to create a table according to the schema and fill in your records. Remember there are validation steps as mentioned in the code.

Task 1
Create tables in your database based on the provided DB schema. Retrieve the necessary database information from the "Database Info" section in the sidebar. Once the tables are created, populate the database information in the "settings.py" file.

Task 2
In this module, your objective is to create a registration form. You will be given a schema by the data team, and your task is to receive input from the front-end form (similar to a sign-up process), process the data, perform validations, and store the captured data in a database table.

You will implement several functions, including nested functions. These functions will mainly focus on validation, registration, and data capture.

For instance, the function check_email(email) should validate whether the email format is correct, following the pattern something@something.com. If the format is incorrect, the user should be prompted to correct it.

You will use these functions within another function called register to perform validations, and then you will utilize the validated data in the capture function.

Assume that an input string is given to you in the following format:

name_value = 'test_data'

user_name = 'testusername'

email_value = 'testgmail.com'

date_value = '15-12-1999'

password_value = 'testdfs77ds'

registration_form = {'name': name_value, 'username': user_name, 'email': email_value, 'dob': date_value, 'password': password_value}

 

You need to write code as indicated in the comments within the code to validate and capture the data.

Steps:

Examine the provided schema.
Implement the functions as specified in the code comments.
Write validation scripts.
Capture the data in the table.

Module 2
In this module, your objective is to display all available movie shows stored in the database table. You will be provided with the data schema and the necessary data.

Module 3
In this module, assume that the user is selecting a ticket through an interface.

Take the input for the movie ID and the number of tickets from the user.
Implement conditions to validate the inputs and make decisions based on them.
Retrieve availability data from the database and dynamically check the ticket availability.
Upon booking, update the ticket count in the table as specified in the code comments.