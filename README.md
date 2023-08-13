0x00. AirBnB clone - The console

 Project done by: Dennis Mwendwa and Hillary Gor


How to use console.

Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)


Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

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
(hbnb) ** class name missing **
(hbnb)
$
}
