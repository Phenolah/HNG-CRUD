- # HNG-CRUD Documentation
This is a Django project that implements a CRUD (Create, Read, Update, Delete) API for managing person records. It utilizes Django and Django Rest Framework (DRF) to provide a simple API for creating, retrieving, updating, and deleting person records.

- #Endpoints

1.Create a Person

Endpoint: POST /api


Request Format:

<code> {
    "name": "Timbaland"
}
</code>

Response Format (Success):


<code>{
  "id": 8,
  "name": "Timbaland"
}
</code>

2.Retrieve a Person


Endpoint: GET /api/{id}


Response Format (Success):


<code>{
  "id": 8,
  "name": "Timbaland"
}
</code>

3.Update a Person


Endpoint: PUT /api/{id}


Request Format:


<code>{
  "name": "Timbaland"
}
</code>

Response Format (Success):

<code>
{
  "id": 8,
  "name": "Timberland"
}
</code>

4.Delete a Person


 Endpoint: DELETE /api/{id}


Response Format (Success):

<code>
{
  "message": "Person with id 1 has been deleted successfully."
}
</code>