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

