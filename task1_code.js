const { executeQuery } = require('./settings')

// Function to check if a string has numbers or not
function has_numbers(inputString) {
	return null
}

// Function for validating an email
function check_email(email) {
	return null
}

// Form validation
function register(registration_form) {
	//your input from your input string (assume from front end , json)

	//name lenth should be greater than 3 and should not have any digits
	//check email validation here
	//password should be greater than 8 digits and must have numbers, reuse has_number function
	//after validation insert into database
	//create connection

	return null
}

// Function to capture data
async function register_data(registration_form) {
	const data = register(registration_form)

	if (data === true) {
		const name = registration_form['name']
		const email = registration_form['email']
		const username = registration_form['username']
		const date = registration_form['dob']
		const password = registration_form['password']

		// ## check if username already in database, use 'where' clause

		// #if username not taken create a new record, insert values into table
	} else {
		return data
	}
}

/////Do not delete following function
async function run_task() {
	// Test data
	const name = 'testse'
	const username = 'testu'
	const email = 'email@testgmail.com'
	const date = '15-12-1999'
	const password = 'testfffffff22'
	const registration_form = {
		name: name,
		username: username,
		email: email,
		dob: date,
		password: password,
	}
	const res = await register_data(registration_form)
	console.log(res)
}

module.exports = { register_data, run_task }
