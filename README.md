# Packman Package Manager
A simple CLI package manager for python


## Getting Started
To get the application up and running there are some few things you will need to do. Ensure that you have at least installed on your computer. 
``` 
Python 3.9 
``` 

### Design Patterns
This application utilizes the following design patterns:
- The command pattern ( for the implementation of the package installation command)
- Factory pattern for the creation of the `DeletePackage` and `InstallPackage` object instances

To run the application, we will follow the following steps:

### ACTIVATE VIRTUAL ENVIRONMENT
While you can run the application by creating a docker image, you can also run directly via using the Django Admin. To run, from the application root directory, run the following command: to activate the virtual environment

``` bash
$ source/venv/bin/activate

```

Install all required packages

``` bash
$ pip install -r requirements.txt

```
Move to the app directory using:

``` bash
$ cd packman

```
Run packman using: 
``` bash
$ python -m  packman install musicdownloader

```

Enjoy the application!