# WorldChat

![alt text](/static/img/final.jpg)

## Description

A scalable social networking web application built with Flask web framework that
makes it easy for users to connect, chat and share with their friends and family online. 

## Motivation

WorldChat social application was built as my final project for the course I took on Udemy website.
Moreover, when building WorldChat, I considered several techniques that allows me to scale the application better.

## The structure of WorldChat

WorldChat is a modular application that uses the concept of Flask blueprints. 

### Why Blueprints?

Flask uses a concept of blueprints for making application components and supporting common patterns within an application or across applications. Blueprints can greatly simplify how large applications work and provide a central means for Flask extensions to register operations on applications.

Blueprints in Flask are intended for these cases:

* Factor an application into a set of blueprints. This is ideal for larger applications; a project could instantiate an application object, initialize several extensions, and register a collection of blueprints.
* Register a blueprint on an application at a URL prefix and/or subdomain. Parameters in the URL prefix/subdomain become common view arguments (with defaults) across all view functions in the blueprint.
* Register a blueprint multiple times on an application with different URL rules.
* Provide template filters, static files, templates, and other utilities through blueprints. A blueprint does not have to implement applications or view functions.
* Register a blueprint on an application for any of these cases when initializing a Flask extension.

If you want to know more, please take a look at the Flask documentation in the following [link](http://flask.pocoo.org/docs/0.12/blueprints/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

You can simply run(source setup.sh) the [setup.sh](setup.sh) file which installs 
all the libraries listed in [requirements.txt](requirements.txt) file in a  virtual environment.

Finally, modify [settings.py](settings.py.bak) file to fit to your own environment.

## Running the program

Once your development environment is setup, activate your virtual environment and run the application using this command:

```
python manage.py runserver
```

## Running the tests

There are separate test suites for relationship blueprint ([Relationship_test](relationship/tests.py)) and user blueprint ([User_test(user/tests.py)). 
Run unit tests using this command:

```
python tests.py
```

## Built With

* Python Flask Web Framework- The programming language
* MongoDB - NoSQL database
* Amazon Web Services
* Javascript
* Bootstrap



