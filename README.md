# Python FastAPI Project

This is a Python project that uses the FastAPI framework to create a web application. This project is a clone of Twitter, with the following features:

## Features

- User sign up and login
- Creation and retrieval of tweets

## Dependencies

The following packages are required to run this application:

- fastapi
- pydantic
- uuid
- datetime
- typing

## Running the application

To run the application, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/abelarismendy/twitter-fast-api.git
```
2. Navigate to the project directory:
```bash
cd twitter-fast-api
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
uvicorn main:app --reload
```
5. The application will be running at http://localhost:8000.

## Endpoints

The following endpoints are available in the application:

### Users

- POST /signup: Sign up a new user.
- POST /login: Login a user.
- GET /users: Retrieve a list of all users.
- GET /users/{user_id}: Retrieve a specific user.

### Tweets

- POST /tweets: Create a new tweet.
- GET /tweets: Retrieve a list of all tweets.
- GET /tweets/{tweet_id}: Retrieve a specific tweet.

## Data Storage

The application stores data in a JSON file:

- users.json: Stores user data.
- tweets.json: Stores tweet data.
