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
