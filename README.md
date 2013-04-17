flask-api-example
=================

Example of a basic API for a sqllite3 database

###Usage###

The file app.py demonstrates CRUD operations for a table called 'messages' that has two text columns, 'name' and 'comment'.

When the app launches it will check if the database tables already exist, and create them if necessary.

Routes:
<table>
	<tr><td>Route</td><td>Method</td><td>Parameters</td><td>Result (JSON)</td></tr>
	<tr><td>/</td><td>GET</td><td></td><td>Returns 'hello world'</td>
	<tr><td>/messages</td><td>GET</td><td></td><td>Returns all messages</td>
	<tr><td>/messages</td><td>POST</td><td>name=foo&comment=bar</td><td>Creates a new message with the posted values</td></tr>
	<tr><td>/search</td><td>GET</td><td>name=foo</td><td>Returns all messages where name = 'foo'</td></tr>
	<tr><td>/messages/1</td><td>GET</td><td></td><td>Gets the message with id=1</td></tr>
	<tr><td>/messages/1</td><td>POST</td><td>name=foo&comment=bar</td><td>Update the message with id=1</td></tr>
	<tr><td>/messages/1</td><td>DELETE</td><td></td><td>Delete the message with id=1</td></tr>
</table>

To create a database based on this file and deploy it to Heroku:
<ol>
	<li>Update app.py according to the tables you want in your database. Specifically, you should change the db_init function so that it creates one or more table(s) with the rows/datatypes you would like. <a href="http://www.sqlite.org/datatype3.html">See here</a> for a list of sqllite3 data types.</li>
	<li>Follow the heroku <a href="https://devcenter.heroku.com/articles/quickstart">getting started guide</a> to install heroku (and git if you don't already have it)</li>
	<li>At the command line, cd into the top-level directory and type <code>heroku create</code>.</li>
	<li>Commit any outstanding changes. If you are unfamiliar with git, check out one of these resources: <a href="http://sixrevisions.com/resources/git-tutorials-beginners/">git tutorials</a></li>
	<li>Type <code>git push heroku master</code></li>
	<li>Heroku will detect that it's a Flask app, deploy it, and return the url of the app. It will be a silly name like mysterious-valley-1203.herokuapp.com. You can rename it to something nicer with <code>heroku apps:rename yournewname</code></li>
</ol>

###Demo###
http://messagestore.herokuapp.com