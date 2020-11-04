# 0x00. AirBnB clone - The console
#### Project to be done in teams of 2 people:
###### Abderrahmen Hidoussi, Oumayma Bougossa
## AirBnB clone:Higher-level programming
![](“logohbnb.png”)

>##### I know you were waiting for it: it’s here!

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
### Concepts to learn
-Unittest - and please work all together on tests cases.
-Python packages concept page.
-Serialization/Deserialization.
-*args, **kwargs.
-datetime.
-More coming soon!.
### Steps
***You won’t build this application all at once, but step by step.
Each step will link to a concept:***
### The console
1.create your data model
2.manage (create, update, destroy, etc) objects via a console / command interpreter
3.store and persist objects to a file (JSON file)
![The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine]("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T085507Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=29a6eb3841744d5cd01346b43dd6ca9d7cfa43d07f94e471f6c5fde9c7f1f82c")
### Web static
1.learn HTML/CSS
2.create the HTML of your application
3.create template of each object
!("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T085507Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=17bb23279b68c24cf1e9782526a1fe2efd4e352cedbd120e3eb3da2588fe2894")
### MySQL storage
1.replace the file storage by a Database storage
2.map your models to a table in database by using an O.R.M.
!("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T085507Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d16975e1c98a4a32229d8f85798c4636f65d38e93eb4cd476eec0e886d554898")
### Web framework - templating
1.create your first web server in Python
2.make your static HTML file dynamic by using objects stored in a file or database
!("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T085507Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fd4bd7ac364a32e55010e914cca35002cab0025c664e242c871de26c004070f0")
### RESTful API
1.expose all your objects stored via a JSON web interface
2.manipulate your objects via a RESTful API
!("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T085507Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fd4bd7ac364a32e55010e914cca35002cab0025c664e242c871de26c004070f0")
### Web dynamic
1.learn JQuery
2.load objects from the client side by using your own RESTful API
!("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T085507Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=23f51a1d63cdf69b6e7b4339c640aac3f0db407c9c29e1eee6044ffd6cb24f34")
## Files and Directories
*models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is *the representation of an object/instance.
*tests directory will contain all unit tests.
*console.py file is the entry point of our command interpreter.
*models/base_model.py file is the base class of all our models. It contains common elements:
*attributes: id, created_at and updated_at
*methods: save() and to_json()
*models/engine directory will contain all storage classes (using the same prototype). For the moment you will have *only one: file_storage.py.

***First step: Write a command interpreter to manage your AirBnB objects.***
>This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
-create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-create the first abstracted storage engine of the project: File storage.
-create all unittests to validate all our classes and storage engine.

## Learning Objectives
### General
*How to create a Python package
*How to create a command interpreter in Python using the cmd module
*What is Unit testing and how to implement it in a large project
*How to serialize and deserialize a Class
*How to write and read a JSON file
*How to manage datetime
*What is an UUID
*What is *args and how to use it
*What is **kwargs and how to use it
*How to handle named arguments in a function
### Requirements
#### Python Scripts
>1.Allowed editors: vi, vim, emacs
2.All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
3.All your files should end with a new line
4.The first line of all your files should be exactly #!/usr/bin/python3
5.A .README.md file, at the root of the folder of the project, is mandatory
6.Your code should use the PEP 8 style (version 1.7 or more)
7.All your files must be executable
8.The length of your files will be tested using wc
9.All your modules should have a documentation (python3 -c 'print('__import__("my_module").__doc__)')
10.All your classes should have a documentation (python3 -c 'print('__import__("my_module").MyClass.__doc__)')
11.All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.'__doc__')' and python3 -c 'print('__import__("my_module").MyClass.my_function.__doc__)')
12.A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
#### Python Unit Tests

>1.Allowed editors: vi, vim, emacs
2.All your files should end with a new line
3.All your test files should be inside a folder tests
4.You have to use the unittest module
5.All your test files should be python files (extension: .py)
6.All your test files and folders should start by test_
7.Your file organization in the tests folder should be the same as your project
8.e.g., For models/base_model.py, unit tests must be in:' tests/test_models/test_base_model.py'
9.e.g., For models/user.py, unit tests must be in:' tests/test_models/test_user.py'
10.All your tests should be executed by using this command: python3 -m unittest discover tests
11.You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
12.All your modules should have a documentation (python3 -c 'print'(__import__("my_module").__doc__)')
13.All your classes should have a documentation (python3 -c 'print'(__import__("my_module").MyClass.__doc__)')
13.All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.'__doc__')' and python3 -c 'print('__import__("my_module").MyClass.my_function.__doc__)')
14.We strongly encourage you to work together on test cases, so that you don’t miss any edge case.

### More Info
#### Execution
Your shell should work like this in interactive mode:
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

But also in non-interactive mode: (like the Shell project in C)
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
!("https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T084800Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bbb1b1f7b44e975a1fdc35099d545d2a0df4dd9558319337f4dde58f55684430")
:mag:### Tasks

:zero:### README, AUTHORS :
*Write a README.md:
*description of the project
*description of the command interpreter:
*how to start it
*how to use it
*examples
*You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
*You should use branches and pull requests on Github - it will help you as team to organize your work
#### Repo:
*GitHub repository: AirBnB_clone
*File: README.md, AUTHORS

:one:### Be PEP8 compliant! :
Write beautiful code that passes the PEP8 checks.
#### Repo:
*GitHub repository: AirBnB_clone
:two: Unittests 
All your files, classes, functions must be tested with unit tests

'''
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
'''
Note that this is just an example, the number of tests you create can be different from the above example.
#### Repo:
*GitHub repository: AirBnB_clone
*File: tests/
:three:###  BaseModel :
***Write a class BaseModel that defines all common attributes/methods for other classes:***

*'models/base_model.py'
*Public instance attributes:
*''id: string - assign with an uuid when an instance is created:
*you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
*the goal is to have unique id for each BaseModel
*'created_at': datetime - assign with the current datetime when an instance is created
*'updated_at': datetime - assign with the current datetime when an instance is created and it will be updated every *time you change your object
*'__str__': should print:' [<class name>] (<self.id>) <self.__dict__>'
*Public instance methods:
*save(self): updates the public instance attribute updated_at with the current datetime
*to_dict(self): returns a dictionary containing all keys/values of '__dict__ 'of the instance:
*by using self.'__dict__', only instance attributes set will be returned
*a key' __class__' must be added to this dictionary with the class name of the object
*created_at and updated_at must be converted to string object in ISO format:
*format: '%Y-%m-%dT%H:%M:%S.%f' '(ex: 2017-06-14T22:31:03.285259)'
*you can use isoformat() of datetime object
*This method will be the first piece of the serialization/deserialization process: create a dictionary representation with '“simple object type” 'of our BaseModel
'''
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'Holberton', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - Holberton
    '__class__': '(<class 'str'>)' - BaseModel
    updated_at: '(<class 'str'>)' - '2017-09-28T21:05:54.119572'
    id: '(<class 'str'>)' - 'b6a6e15c-c67d-4312-9a75-9d084935e579'
    created_at:' (<class 'str'>) '- '2017-09-28T21:05:54.119427'

guillaume@ubuntu:~/AirBnB$ 
'''
#### Repo:
*GitHub repository: AirBnB_clone
*File: 'models/base_model.py', 'models/__init__.py, tests/'
:four:###Create BaseModel from dictionary:
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.
'''
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
'''
*Update models/base_model.py:
*'__init__(self, *args, **kwargs)':
*you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
*'*args' won’t be used
*if 'kwargs' is not empty:
*each key of this dictionary is an attribute name (Note '__class__' from kwargs is the only one that should not be *added as an attribute. See the example output, below)
*each value of this dictionary is the value of this attribute name
*Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
*otherwise:
*create id and created_at as you did previously (new instance)
'''
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'Holberton'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'Holberton'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - Holberton
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'Holberton'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$ 

'''
#### Repo:
*GitHub repository: AirBnB_clone
*File: models/base_model.py, tests/

:five:### Store first object:

Now we can recreate a BaseModel from another one by using a dictionary representation:
'''
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
'''

***It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.***

***Writing the dictionary representation to a file won’t be relevant:***

*Python doesn’t know how to convert a string to a dictionary (easily)
*It’s not human readable
*Using this file with another program in Python or other language will be hard.
***So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.***

***Now the flow of serialization-deserialization will be:***

'''
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
'''

***Magic right?***

***Terms:***



