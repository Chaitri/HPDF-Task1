# HPDF-Task1
Demonstration of required tasks using Python-Flask.

## Installation

Install Python from the [official website](https://www.python.org/downloads/). Installation of Flask can be done by following through [this document](http://flask.pocoo.org/docs/0.12/installation/). 

## Execution

To run the application, use the **python** command :
```
python main.py
```
This launches a very simple builtin server; head over to http://127.0.0.1:5000/ to see the Hello, World greeting. 

## Tasks

- Visiting http://127.0.0.1:5000/ will display a simple Hello, World - Chaitri string.
- Visiting http://127.0.0.1:5000/authors  will respond with a list of authors and the count of their posts where the list of authors are fetched from a request to https://jsonplaceholder.typicode.com/users and the list of posts are fetched from a request to https://jsonplaceholder.typicode.com/posts.
- Visiting http://127.0.0.1:5000/setcookie will set cookies with a name and age value.
- Visiting http://127.0.0.1:5000/getcookies will fetch the cookies and display their key-value pairs.
- Visiting http://127.0.0.1:5000/robots.txt will be denied.
- Visiting http://127.0.0.1:5000/html will render a simple HTML template.
- Visiting http://127.0.0.1:5000/input will display a text field where any user input can be entered, and on submission, will display the entered input. 
