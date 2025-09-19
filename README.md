Phase 3 Project: CLI and ORM
Learning Goals
Implement a Python application that includes a Command Line Interface.
Implement a set of Object-Relational Mapping functions for two or more model classes.
Define a Python object model that includes a one-to-many relationship between two classes.
Exercise best practices in CLI design.
Exercise best practices in OOP.
Key Vocab
Command Line: a text-based interface that is built into your computer's operating system. It allows you to access the files and applications on your computer manually or through scripts.
Terminal: the application in Mac OS that allows you to access the command line.
Command Shell/Powershell: the applications in Windows that allow you to access the command line.
Command-Line Interface (CLI): a text-based interface used to run programs, manage files and interact with objects in memory. As the name suggests, it is run from the command line.
Object-Relational Mapping (ORM): a programming technique that provides a mapping between an object-oriented data model and a relational database model.
Attribute: variables that belong to an object.
Property: attributes that are controlled by methods.
Decorator: function that takes another function as an argument and returns a new function with added functionality.
Introduction
Welcome to the end of Phase 3! You've learned about a lot in this unit:

Python fundamentals.
Data structures (and more recently, algorithms).
Object-oriented programming.
Object inheritance.
Instance and class attributes and methods.
Configuring applications.
SQL fundamentals.
Table relations in SQL.
Object-relational mapping with Python.
Building CLIs.
The Phase 3 project is open-ended when it comes to the actual content. You are free to create whatever you'd like, as long as it incorporates the requirements listed below.

Requirements
In the previous lab and code-along, we created a command line interface to be used by a developer for testing of their ORM methods. For this project, we want you to select a different type of user and build your own CLI and its helper methods that show the user client-facing information.  Think about the user experience.  How can it be made easier for the user to use?  Your options in the CLI will not just be one long list of choices.  If it is a recipe box app, if the user is looking at Desserts and wants to add a recipe they should be able to do it there without being asked again what category the recipe is in - they are looking at the desserts category!  Don’t show the user backend information like database IDs and the objects returned formatted by the model repr method - that is developer information.  The CLI and its helper methods represent the frontend of your project - just as you did not show the user json in your phase 2 project, you wouldn’t show the user the python objects sent from the backend.  And it is in the frontend (CLI and helpers) that the formatting is done.  The CLI and helpers should be created by you - not a copy of our CLI and helpers simply changed to reflect your models. They were appropriate for our developer testing their ORM methods but you should write your own CLI and helpers that are appropriate for your user story and models. Be creative!

ORM Requirements
The application must include a database created and modified with Python ORM methods that you write.

The data model must include at least 2 model classes.
The data model must include at least 1 one-to-many relationship.
Property methods should be defined to add appropriate constraints to each model class.
Each model class should include ORM methods (create, delete, get all, and find by id at minimum).
CLI Requirements
The CLI must display menus with which a user may interact.
The CLI should use loops as needed to keep the user in the application until they choose to exit.
For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
The CLI should validate user input and object creations/deletions, providing informative errors to the user.
The project code should follow OOP best practices.
Pipfile contains all needed dependencies and no unneeded dependencies.
Imports are used in files only where necessary.
Project folders, files, and modules should be organized and follow appropriate naming conventions.
The project should include a README.md that describes the application.
You do not need to implement tests for pytest, although you should test your code thoroughly using your CLI. Try entering bad data when prompted for input, and confirm your application prints a useful error message.

How to begin?
Start with the project template (provided in the following lesson). You are free to adapt the template structure, as long as you adhere to the project requirements.
Think about the user interaction. How will you prompt the user? What information will the user enter? How will you provide feedback to the user?
Think about your data model. How will you organize and store the information received from the user?
If you get stuck trying to accomplish a specific task, check online to see if there's a Python library that will make it easier.
Consider using ClickLinks to an external site. or FireLinks to an external site. to take care of basic CLI tasks for you.

# Laptop Store CLI + ORM

This is a command-line interface (CLI) application to manage a laptop store using Python and SQLite.

## Features
- Manage categories (create, list, delete)
- Manage laptops (create, list, delete, view by category)
- ORM-style methods with SQLite database

<!-- ## How to run
```bash
python main.py
``` -->

The database file (`laptops.db`) will be created automatically.


