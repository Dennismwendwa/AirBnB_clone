0x00. AirBnB clone - The console

Description.
HBnB is a clone of AirBnB's command interpreter. This project focuses on the backend.
First step, is to write a parent class to take care of the initialization, serialization
and deserialization of future instances. Second step, to create a flow of 
serialization/deserialization: Instance<->Dictionary<->JSON string,<->file

What is a command interpreter?
A command interpreter is the part of the operating system that takes commands via the
command line from the user and executes them. The Shell is an example of one

Project Scope
With HBnB, the user can create Users, Places, States, Cities, and Reviews, as well as update each
class with attributes such as name, first_name, last_name, email, and password. Below is a table
with all functionality of the console:

Command 	Description
create 		creates a new instance of a class
show 		shows instance of a specified class or all class instances
destroy 	deletes an instance based on class name and id
all 		prints all string representations of all instances
update 		updates an instance of a class ie email attribute of a User


Examples of using the console in interactive mode:
{
$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create
** class name missing **

(hbnb) create BaseModel
138486be-3e76-43c8-b4f0-59f8c4888e87

(hbnb) show
** class name missing **

(hbnb) create User
e16d4b4d-9320-408c-90f4-0752be7fa65d

(hbnb) all
{'BaseModel.e12c8168-bad8-4ac1-b685-f8bcc1a57bed': <models.base_model.BaseModel object at 0x7f6d0780c780>,}
(hbnb)
}


Examples of using the console in non-interactive mode:
{
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)

$ echo show | ./console.py
(hbnb) ** class name missing **
(hbnb)


$ echo all | ./console.py
(hbnb) {'BaseModel.14dd894f-da3b-4e40-84a0-03b558ff80f1':
(hbnb)
$
}
