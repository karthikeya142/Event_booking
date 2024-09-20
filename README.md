# Event Booking System

## Overview

This is a Django-based Event Booking System that allows users to view events, register, log in, and book tickets for events. 
It provides an easy-to-use interface for managing events and bookings.

## Features

- User registration and authentication
- View a list of available events
- Event details and booking functionality
- Booking status display
- Admin interface for adding new events

## Requirements

- Python 3.x
- Django 4.x
- A database (e.g., SQLite, PostgreSQL)

## Installation
```sh
pip install django
```



Creating A Django Project
Open cmd
```sh
  django-admin startproject Event_book
   ```
 create a first Django Event_book the app.
```sh
django-admin startapp webapp
```
Running Django Project On Localhost
```sh
python manage.py runserver
```
the process of creating tables out of a Django model is called as making migrations.
```sh
python manage.py makemigrations
```
create those tables, you need to type in another command.
```sh
python manage.py migrate
```

install virtual environment on your computer, be it Windows or Mac, you need to go:-
```sh
pip install virtualenv
```
on windows go to the dir env/scripts
 whenever you want to activate the environment:-
```sh
 .\activate 
 ```
 whenever you want to deactivate the environment:-
```sh
  .\deactivate 
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Creating Model:-
we need to do here is that once you have created the models, you have to make migrations,
But even before you make migrations, you first need to go ahead and make sure that
you have added your my app into your settings.py file or else the migrations are not going to work.
simply go ahead and type in my app in the installed apps directory of the settings.py
We have added the app name here, we are now free to go ahead and make migrations.it will create the model called as task. 
```shell
python manage.py makemigrations
```
once you have made the migrations, you then need to type
 ```sh 
 python3 manage.py migrate
 ```
all the migrations have been applied and a new model which is called as Event

we have successfully completed the first feature or the first feature implementation of adding a event model

need to go ahead and log in into your admin site now in order to log in into your admin site,
order to create a super user, type  
```sh 
Python Manage.py createsuperuser
```
giving usrname: Event

give dummy mail: Event@gmail.com

password : Event123

Superuser created successfully. run server
login :http://localhost:8000/


Usage
Home Page: Welcome message and navigation.
Register: Create a new account.
Login: Authenticate users.
Event List: Browse available events.
Event Detail: View details and book tickets for an event.
Booking Status: View the status of your booking.
Contributing
Contributions are welcome! Please feel free to submit a pull request.

License
This project is licensed under the MIT License.

Author
B Karthik Kumar Reddy


Feel free to let me know if you need any more changes!
