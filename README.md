# API CRUD RESTAURANT

*This is a Flask API CRUD with an interface to improve the user experience.*

## Starting! 🚀

*These instructions will help you to run this project locally.*

## Requirements 📋

*Use git clone o download zip to have this project in your machine*
*Navigate to the carpet of the project*

### Virtual environments
*You need create a virtual environment (Windows): *
```
pip install virtualenv
virtualenv venv 
```
*Now, you need to activate the virtual environment (Windows and PowerShell): *
```
.\venv\Scripts\activate
```

### How to install the packages?
*Inside the project there is a file called **requirements.txt**, this file can be used to install
the necessaty packages that the project needs.*

*You need type the next command inside a terminal like: **CMD or Powershell**: *
```
pip install -r requirements.txt
```
**You must navigate to the root of the project**

## Configuration additional
*The file db.py has my credentials to connect to MySQL, it is neccesary to change those data*

## DB Included
*I have included the file DBRestaurantsApp.sql to get the database and the stored procedure that you need to work with the project*

**This file can be import from Workbench MySQL**

## How to run the project? ⚙️

### Way 1

*You can run the project with the next commands (CMD): *
```
> set FLASK_APP=main
> flask run
 * Running on http://127.0.0.1:5000/
 ...
 ...
```

*If you use PowerShell: *
```
> $env:FLASK_APP = "main"
> flask run
 * Running on http://127.0.0.1:5000/
 ...
 ...
```

### Way 2

*Use the file main.py to run the project: *
```
> python main.py
 * Running on http://127.0.0.1:5000/
 ...
 ...
```

## Interface included 💻

*When you run the project with any of the ways in the previous section, you can see a URL
**http://127.0.0.1:5000/**, the port can be different, navigate to the URL and you will see
the interface to perform CRUD operations*

![Alt text](./src/static/images/example.png?raw=true "Interface")


