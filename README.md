# HNG-CRUD
This is a Django project that implements a CRUD (Create, Read, Update, Delete) API for managing person records. It utilizes Django and Django Rest Framework (DRF) to provide a simple API for creating, retrieving, updating, and deleting person records.

## Prerequisities
Before you begin, ensure you have met the following requirements:

- Python 3.x installed locally.


- Virtual environment (`venv`) or `pipenv` for managing dependencies.


- Basic understanding of Django and Django Rest Framework.

# Steps to run
##Clone the github repo

https://github.com/Phenolah/HNG-CRUD

##Create a virtual environment

From your terminal, navigate into the ProfileProject directory and create a virtual environment using 
<code> python -m venv venv </code>
Activate the virtual environment


##Activate the virtual environment using 


<code>.\venv\Scripts\activate </code> on windows and source venv/bin/activate  for mac and Linux


##Install requirements

All requirements for this projects are located in the requirements.txt file, install all of them using the command <code> pip install -r requirements.txt</code>


##Configuration
Create a .env file in the project root directory and configure the following settings
<code>
DEBUG=True
SECRET_KEY=your-secret-key
</code>


##Database 
 Configure your database settings in <code>ProfileProject/settings.py</code>


##Run the server

From your terminal, enter into the backend folder, this is the root directory for the project

Run <code>python manage.py runserver</code> to get the server running on your specified port or 
<code> python manage.py runserver </code> to get the server running on the default port which is 8000


##Make migration

From your terminal, ensure you are in the root directory of the project which is the backend folder and run the following commands
<code> python manage.py makemigrations
python manage.py migrate </code>

Access the api

Your api should now be accesible on <code> localhost:<port>/api</code> For a detailed guide on how to use the endpoints in this project, refer to the DOCUMENTATION.md file located within this project

##Access the api

Your api should now be accesible on <code>localhost:<port>/api. </code> For a detailed guide on how to use the endpoints in this project, refer to the https://github.com/Phenolah/HNG-CRUD/blob/main/documentation.md file located within this project