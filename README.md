# Spy Cat Agency Backend

This is the backend API for the Spy Cat Agency application, built with Django
and Django REST Framework.

## Table of Contents

- [Setup](#setup)
- [Running the Development Server](#running-the-development-server)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [Using Postman](#using-postman)

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
    - Windows:
      ```
      venv\Scripts\activate
      ```
    - macOS/Linux:
      ```
      source venv/bin/activate
      ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

## Running the Development Server

To start the development server:

```
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/api/v1/

## Authentication

The API uses token-based authentication. To authenticate:

1. Obtain a token by sending a POST request to `/api/v1/accounts/login/` with
   your credentials:
   ```json
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. The server will respond with a token:
   ```json
   {
     "token": "your_auth_token"
   }
   ```

3. Include this token in the Authorization header of all subsequent requests:
   ```
   Authorization: Token your_auth_token
   ```

### Cat Management

New cats can be created via API. As a temporary solution the username and
password for Cat user printed to the console

## API Endpoints

### Authentication

- `POST /api/v1/accounts/login/` - Obtain authentication token

### Cats

- `GET /api/v1/cats/` - List all cats
- `POST /api/v1/cats/` - Create a new cat
- `GET /api/v1/cats/{id}/` - Retrieve a specific cat
- `PATCH /api/v1/cats/{id}/` - Update the cat salary
- `DELETE /api/v1/cats/{id}/` - Delete a specific cat

### Missions

- `GET /api/v1/missions/` - List all missions
- `POST /api/v1/missions/` - Create a new mission
- `GET /api/v1/missions/{id}/` - Retrieve a specific mission
- `POST /api/v1/missions/{id}/assign` - Assign Cat to the mission
- `DELETE /api/v1/missions/{id}/` - Delete a specific mission

### Targets

- `GET /api/v1/missions/targets/{id}/complete` - Complete a specific target
- `POST /api/v1/missions/targets/{id}/note` - Add note to a specific target

## Using Postman

There is a link to the Postman API:
https://www.postman.com/solutionskus/yaroslav-s-public-workspace/collection/b1tzmvz/spy-cat-agency?action=share&creator=30312139
