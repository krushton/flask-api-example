flask-api-example
=================

Example of a basic API for a sqllite3 database

##Usage##

###db_init.py###

The db_init.py script can be used to quickly add tables to the database (called data.db and stored in the root directory by default).

The format of the command line arguments is: 
<code>python db_init.py tablename columnname:type columnname:type columnname:type ...</code>

For example, to create a table called Books that will have a column for title, number of pages, and price:

<code>python db_init.py books title:text pages:int price:real</code>

See <a href="http://www.sqlite.org/datatype3.html">here</a> for a list of sqllite types.

###app.py###

This file demonstrates CRUD operations for a table called 'messages' that has two text columns, 'name' and 'comment'.

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

