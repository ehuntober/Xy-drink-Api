#  Xy-Drink
## API documentation!

Welcome to the Drink API documentation! This API allows you to retrieve information about drinks, as well as create, update, and delete drinks.

### Base URL
The base URL for this API is https://127.0.0.1:8000/drinks/

### Authentication
Authentication is not required to use this API.
### Endpoints
#### GET /drinks
This endpoint retrieves a list of all drinks.

##### Response
- `200 OK`: Returns a list of drinks containing the name and description of each drink. 

Response
```json
{
    "drinks": [
        {
            "id": 1,
            "name": "Espresso",
            "description": "A concentrated coffee beverage brewed by forcing hot water under high pressure through finely ground coffee."
        },
        {
            "id": 2,
            "name": "Latte",
            "description": "A coffee drink made with espresso and steamed milk."
        },
    
    ]
}
```

#### GET /drinks/{id}
This endpoint retrieves information about a specific drink.

#### Parameters
- `id (required)`: The ID of the drink to retrieve.

#### Response
- `200 OK`: Returns information about the specified drink, including the name and description.

##### Example Response:

```json
{
    "id": 2,
    "name": "Latte",
    "description": "A coffee drink made with espresso and steamed milk."
}
```
- `404 Not Found`: If the specified drink ID does not exist.

### POST /drinks
This endpoint creates a new drink.

#### Parameters
- `name (required)`: The name of the new drink.
- `description (required)`: A description of the new drink.

### Response
- `201 Created`: Returns information about the newly created drink, including the ID, name, and description.

#####  Example Response:
```json
{
    "id": 4,
    "name": "Cappuccino",
    "description": "A coffee drink made with espresso and steamed milk foam."
}
```

### PUT /drinks/{id}
This endpoint updates an existing drink.

#### Parameters
- `id (required)`: The ID of the drink to update.
- `name (optional)`: The new name of the drink.
-  `description (optional)`: The new description of the drink.

##### Response
- `200 OK` : Returns information about the updated drink, including the ID, name, and description.

##### Example Response:

```json
   {
    "id": 2,
    "name": "Latte",
    "description": "A coffee drink made with espresso and steamed milk foam.."
}
```
- `404 Not Found` : If the specified drink ID does not exist.

## DELETE /drinks/{id}
This endpoint deletes an existing drink.

#### Parameters
- `id (required)`: The ID of the drink to delete.

#### Response
- `204 No Content`: Returns no content if the specified drink was successfully deleted.

- `404 Not Found`: If the specified drink ID does not exist.

## Conclusion
That's it! This documentation should provide you with all the information you need to use the xy Drink API. If you have any questions or feedback, please don't hesitate to contact us.




## Xy-Drink API Installation

Thank you for choosing the Xy-Drink API, which is built with Django REST framework. Here are the steps to get the API up and running.

## Prerequisites
- Python 3.7 or later
- pip package manager

## Installation
1. Clone the repository from Github: git clone `https://github.com/ehuntober/xy-drink-Api.git`
2. Navigate into the project directory: `cd drink-api`
3. Install the required dependencies: pip install -r `requirements.txt`
4. Create a new user with privileges to the database: `createuser --interactive --pwprompt`
5. Run database migrations: `python manage.py migrate`
6. (Optional) Create a superuser for the Django admin interface: `python manage.py createsuperuser`
7. Start the Django development server: `python manage.py runserver`
8. The API should now be accessible at `http://localhost:8000/drinks/`

## Usage
You can use the Drink API with any REST client or HTTP library. For example, you can use the curl command to retrieve a list of drinks:

`curl http://localhost:8000/api/drinks/`

This should return a JSON response containing a list of drinks.

# Conclusion
That's it! You have successfully installed and started the Drink API. If you have any questions or feedback, please don't hesitate to contact us.




