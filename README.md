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