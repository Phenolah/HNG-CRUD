# HNG-CRUD
This is a Django project that implements a CRUD (Create, Read, Update, Delete) API for managing person records. It utilizes Django and Django Rest Framework (DRF) to provide a simple API for creating, retrieving, updating, and deleting person records.

## Prerequisities
Before you begin, ensure you have met the following requirements:

- Python 3.x installed locally.


- Virtual environment (`venv`) or `pipenv` for managing dependencies.


- Basic understanding of Django and Django Rest Framework.

## Steps to run
- Clone the github repo

https://github.com/Phenolah/HNG-CRUD

- Create a virtual environment


- From your terminal, navigate into the ProfileProject directory and create a virtual environment using 
'''python -m venv venv'''
Activate the virtual environment


- Activate the virtual environment using 


.\venv\Scripts\activate on windows and source venv/bin/activate  for mac and Linux


- Install requirements

All requirements for this projects are located in the requirements.txt file, install all of them using the command pip install -r requirements.txt


- Configuration
Create a .env file in the project root directory and configure the following settings
DEBUG=True
SECRET_KEY=your-secret-key


- Configure your database settings in ProfileProject/settings.py.


- Run the server

From your terminal, enter into the backend folder, this is the root directory for the project

Run python manage.py runserver <port> to get the server running on your specified port or python manage.py runserver to get the server running on the default port which is 8000

Make migrations


- From your terminal, ensure you are in the root directory of the project which is the backend folder and run the following commands
python manage.py makemigrations
python manage.py migrate

https://github.com/Phenolah/HNG-CRUD/blob/main/documentation.md


- Access the api

Your api should now be accesible on localhost:<port>/api. For a detailed guide on how to use the endpoints in this project, refer to the https://github.com/Phenolah/HNG-CRUD/blob/main/documentation.md file located within this project