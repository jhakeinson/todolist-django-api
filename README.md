# Todo List Django API

This is a Django REST Framework app that serves the API for [Todo List React Native](https://github.com/jhakeinson/todolist-react-native).

## Prerequisites

- Python 3.x
- pip

## Installation

1. Clone the repository.
2. Create a virtual environment: `python3 -m venv env`
3. Activate the virtual environment: `source env/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`

## Usage

1. Start the development server: `python manage.py runserver`
2. Run the [Todo List React Native](https://github.com/jhakeinson/todolist-react-native).


## Endpoints

### Authentication

#### `POST /api/auth/login`

This endpoint is used for user authentication.

#### `POST /api/auth/register`

This endpoint is used for user registration.

#### `POST /api/auth/refresh`

This endpoint is used for refreshing user authentication tokens.

### Todo

#### `GET /api/todo`

This endpoint is used to retrieve a list of all todos.

#### `GET /api/todo/{id}`

This endpoint is used to retrieve a specific todo by ID.

#### `POST /api/todo`

This endpoint is used to create a new todo.

#### `PUT /api/todo/{id}`

This endpoint is used to update a specific todo by ID.

#### `DELETE /api/todo/{id}`

This endpoint is used to delete a specific todo by ID.

I hope this helps! Let me know if you have any further questions.


