const { executeQuery } = require('./settings')

// Task 2
async function display_shows() {
	try {
		// Dynamically fetch shows from movie table and display
		// The name of the table is movies
		// Use SQL to fetch shows by selecting movie_id, movie_name, show_time, date
		const return_dict = {}
		const my_list = []

		return_dict['show'] = my_list

		// Result: list of objects with keys 'movie_id', 'movie', 'show_time', 'date'
		return return_dict
	} catch (error) {
		throw error
	}
}

async function run_task() {
	const res = await display_shows()
	console.log(res)
}

module.exports = { display_shows, run_task }
