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

To deploy a database on the web using this file:
<ol>
	<li>Update app.py according to the tables you want in your database. Specifically, you should change the <code>db_init()</code> function so that it creates one or more table(s) with the rows/datatypes you would like. <a href="http://www.sqlite.org/datatype3.html">See here</a> for a list of sqllite3 data types.</li>
	<li>Create an account at <a href="https://www.pythonanywhere.com">Python Anywhere</a>. The URL for your app will default to username.pythonanywhere.com.</li>
	<li>At the Python Anywhere welcome screen, click <b>I want to make a web app</b>.</li>
	<li>Click the <b>Web</b> tab.</li>
	<li>Click <b>Add a new web app</b></li>
	<li>Click <b>Next</b> in the wizard.</li>
	<li>Click <b>Flask</b>.</li>
	<li>Edit the text in the Path box to <code>/home/[your user name]/app.py</code></li>
	<li>Click <b>Next</b>. Wait while the app is created. This may take a minute.</li>
	<li>Click the <b>Files</b> tab.</li>
	<li>Click the edit button next to app.py</li>
	<li>Replace the contents of their app.py file with yours, then click <b>Save</b></li>
	<li>In the <b>Web</b> tab, click <b>Reload</b></li>
	<li>The app should now be up and running. To test, go to http://yourname.pythonanywhere.com/ and make sure you see "Hello World". Then go to http://yourname.pythonanywhere.com/messages and verify that you see an empty array [] (since no messages have been added yet).</li>
</ol>

###Demo###
http://krushton.pythonanywhere.com