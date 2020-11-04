# 0x00. AirBnB clone - The console 
:books:  Foundations - Higher-level programming ― AirBnB clone

:couple:Project to be done in teams of 2 people:
###### Abderrahmen Hidoussi, Oumayma Bougossa.

## Welcome to the AirBnB clone project! (The Holberton B&B) :loudspeaker:

### First step: :eyes:  Write a command interpreter to manage your AirBnB objects.

**This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…**
**Each task is linked and will help you to:**
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine.

### What’s a command interpreter :question:

**Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:**
- Create a new object (ex: a new User or a new Place).
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…).
- Update attributes of an object.
- Destroy an object.


## :dart: Learning Objectives 


### General

1. How to create a Python package
2. How to create a command interpreter in Python using the cmd module
3. What is Unit testing and how to implement it in a large project
4. How to serialize and deserialize a Class
5. How to write and read a JSON file
6. How to manage datetime
7. What is an UUID
8. What is *args and how to use it
9. What is **kwargs and how to use it
10. How to handle named arguments in a function


## Requirements


### :snake:  Python Scripts
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file, at the root of the folder of the project, is mandatory
6. Your code should use the PEP 8 style (version 1.7 or more)
7. All your files must be executable
8. The length of your files will be tested using wc
9. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
10. All your classes should have a documentation (python3 -c 'print(__import__("my_module").11. MyClass.__doc__)')
12. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
13. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


## :page_facing_up:      Python Unit Tests

'''
1. Allowed editors: vi, vim, emacs
2. All your files should end with a new line
3. All your test files should be inside a folder tests
4. You have to use the unittest module
5. All your test files should be python files (extension: .py)
6. All your test files and folders should start by test_
5. Your file organization in the tests folder should be the same as your project
6. e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
7. e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
8. All your tests should be executed by using this command: python3 -m unittest discover tests
9. You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
10. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
11. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
12. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
13. We strongly encourage you to work together on test cases, so that you don’t miss any edge case.


## :white_check_mark:     Execution 

**Your shell should work like this in interactive mode:**
'''
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
'''

**But also in non-interactive mode: (like the Shell project in C)**
'''
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
'''

## :computer:   Tasks



