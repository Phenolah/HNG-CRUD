# HNG-CRUD Documentation
This is a Django project that implements a CRUD (Create, Read, Update, Delete) API for managing person records. It utilizes Django and Django Rest Framework (DRF) to provide a simple API for creating, retrieving, updating, and deleting person records.

- Endpoints
Create a Person
Endpoint: POST /api
Request Format:
{
    "name": "Timbaland"
}
Response Format (Success):
{
  "id": 8,
  "name": "Timbaland"
}


- Retrieve a Person
Endpoint: GET /api/{id}
Response Format (Success):
{
  "id": 8,
  "name": "Timbaland"
}


- Update a Person
Endpoint: PUT /api/{id}
Request Format:
{
  "name": "Timbaland"
}
Response Format (Success):
{
  "id": 8,
  "name": "Timberland"
}


- Delete a Person
Endpoint: DELETE /api/{id}
Response Format (Success):
{
  "message": "Person with id 1 has been deleted successfully."
}