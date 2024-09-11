#!/usr/bin/env python3
"""
A simple Flask web application that renders an HTML template.

This script uses Flask to create a web server with a single route, which renders
a template (`0-index.html`) and passes a title variable to the template.

Usage:
    Run this script to start the Flask development server.
    The server will run locally, and you can access it via `http://127.0.0.1:5000/`.

Dependencies:
    - Flask must be installed (`pip install flask`).
"""

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
	"""
	Render the index page of the web application.

	This function is linked to the root URL ("/"). When accessed, it renders the 
	'0-index.html' template and passes a title variable to the template.

	Returns:
		A rendered HTML template ('0-index.html') with a title 'Welcome to Holberton'.
	"""
	return render_template('0-index.html', title='Welcome to Holberton')

if __name__ == '__main__':
	"""
	Start the Flask development server if the script is run directly.

	The server will run in debug mode and be accessible at `http://127.0.0.1:5000/`.
	"""
	app.run()
