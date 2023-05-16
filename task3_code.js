const { executeQuery } = require('./settings')

// Select ticket and IDs
async function select_movie(movie_id, no_of_tickets) {
	try {
		// ##take movie id and no of tickets as inputs

		// ## only 5 tickets for a person condition validation

		// ##select movie_id and avaibility from the database

		// ##validate if a particular movie id is available

		// ## Display how many tickets available

		// ## assume that payment gateway has processed (at the counter)

		// #update the tickets dynamically into database (Change the type to int) (tickets available - ticket booked)

		// ## this is to maintain realistic records

		// ## write update query, change from int to string record where movie_id = 'value'

		// #return True when success
		// #default return should be False
		return False

		// ##challenge since the ticket count is in varchar format in table, you have to dynamically convert type and validate
	} catch (error) {
		throw error
	}
}

// Example usage

async function run_task() {
	const res = await select_movie(1001, 15)
	console.log(res)
}

module.exports = { select_movie, run_task }
