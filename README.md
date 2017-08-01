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


### Prerequisites

What things you need to install the software and how to install them

```

```

### Installing

You can simply run the [setup.sh](setup.sh) file which installs all the dependecies for you.

Or

Install it without running the setup file:

a) Installing Python 2.7
```
Download Python2.7 from Python website: https://www.python.org/downloads/
```

b) Install Tkinter Library

```
You can install Tkinter by simply typing this command in the terminal(linux):
sudo apt-get install python-tk
```


## Running the program

In order to run the program, you just need to run [main.py](main.py) file. You can run it from your IDE or terminal.
Make sure you are inside this directory. In the terminal, type:
python [main.py](main.py)

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```


## Built With

* [Python](https://www.python.org/) - The programming language
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - Python Graphical User Interface Library


## Authors

* **Sher Sanginov**



## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **StackOverflow**