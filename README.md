# FastAPI MySQL Web Application

This project is a web application built using FastAPI, SQLAlchemy, and MySQL. It follows the MVC (Model-View-Controller) design pattern and provides endpoints for user authentication and post management. The application includes field validation, dependency injection, and token-based authentication.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Docker Setup](#docker-setup)

## Project Structure

```
my_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── posts.py
│   └── services/
│       ├── __init__.py
│       ├── auth_service.py
│       ├── post_service.py
├── .env
├── requirements.txt
└── Dockerfile
```

## Features

- **User Signup and Login**: Register and authenticate users.
- **Post Management**: Create, retrieve, and delete posts.
- **Token-based Authentication**: Secure API endpoints using JWT tokens.
- **Field Validation**: Ensure data integrity using Pydantic models.
- **In-memory Caching**: Cache responses for enhanced performance.
- **Dependency Injection**: Efficiently manage dependencies.

## Installation

### Prerequisites

- Python 3.9+
- Docker and Docker Compose

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Set up the virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Configure environment variables in the `.env` file:

    ```env
    DATABASE_URL=mysql+pymysql://cms_api:cms_api@localhost:3306/cms_api_test
    JWT_SECRET=secret
    ```

## Usage

### Running the Application Locally

1. Ensure MySQL is running and accessible with the configured credentials.

2. Initialize the database:

    ```bash
    python -m app.database
    ```

3. Start the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

4. Access the application at `http://localhost:8000`.

### Running with Docker

1. Build and run the Docker containers using Docker Compose:

    ```bash
    docker-compose up --build
    ```

2. Access the application at `http://localhost:8000`.

## API Endpoints

### Signup

- **URL**: `/signup`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "jwt_token",
    "token_type": "bearer"
  }
  ```

### Login

- **URL**: `/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "jwt_token",
    "token_type": "bearer"
  }
  ```

### Add Post

- **URL**: `/add_post`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer jwt_token`
- **Request Body**:
  ```json
  {
    "text": "This is a new post"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "text": "This is a new post",
    "user_id": 1
  }
  ```

### Get Posts

- **URL**: `/get_posts`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "text": "This is a new post",
      "user_id": 1
    }
  ]
  ```

### Delete Post

- **URL**: `/delete_post/{post_id}`
- **Method**: `DELETE`
- **Headers**: `Authorization: Bearer jwt_token`
- **Response**:
  ```json
  {
    "detail": "Post deleted"
  }
  ```

## Environment Variables

- `DATABASE_URL`: Database connection URL.
- `JWT_SECRET`: Secret key for JWT token generation.
- `ALLOW_EMPTY_PASSWORD`: Set to `yes` for MySQL container.

## Docker Setup

1. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

2. Access the application at `http://localhost:8000`.
