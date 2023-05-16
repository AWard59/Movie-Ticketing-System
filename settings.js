const mysql = require('mysql2')

// Following function will create a MySQL connection.
function mysql_connection() {
	// Get your DB connection from "DataBase Info" Tab
	const HOST = 'localhost'
	const USERNAME = 'USERNAME'
	const PASSWORD = 'PASSWORD'
	const DATABASE = 'DATABASE'

	const connection = mysql.createConnection({
		host: HOST,
		user: USERNAME,
		password: PASSWORD,
		database: DATABASE,
	})

	return connection
}

function executeQuery(query, list) {
	return new Promise((resolve, reject) => {
		const connection = mysql_connection()

		connection.query(query, list, (error, results, fields) => {
			if (error) {
				reject(error)
			} else {
				resolve(results)
			}
			connection.end()
		})
	})
}

module.exports = { executeQuery }
