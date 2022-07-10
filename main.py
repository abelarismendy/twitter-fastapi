# Python
import json
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI, status, Body

app = FastAPI()

# Models

class PasswordMixin(BaseModel):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="password",
    )


class UserBase(BaseModel):
    user_id : UUID = Field(...)
    email : EmailStr = Field(...)


class User(UserBase):
    first_name : str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    last_name : str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    birth_date : Optional[date] = Field(default=None)


class UserRegister(PasswordMixin, User):
    pass


class UserLogin(PasswordMixin, UserBase):
    pass


class Tweet(BaseModel):
    tweet_id : UUID = Field(...)
    user_id : UUID = Field(...)
    content : str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at : Optional[datetime] = Field(default=None)


# Routes

@app.get(
    path="/",
)
def home():
    return {"message": "Hello World"}

## Users

### Register a new user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new user",
    tags=["Users"],
)
def signup(user: UserRegister = Body(...)):
    """
    Sign up a new user

    This endpoint allows you to sign up a new user.

    Parameters:
    - Request body:
        - user: UserRegister

    Returns:
    - User: The newly created user with the following fields:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: Optional[date]
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        users = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        users.append(user_dict)
        f.seek(0)
        f.write(json.dumps(users, indent=4))
        return user


### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"],
)
def login():
    pass

### Get all users
@app.get(
    path="/users/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    tags=["Users"],
)
def get_users():
    pass

### Get a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get a user",
    tags=["Users"],
)
def get_user():
    pass

### Update a user
@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"],
)
def update_user():
    pass

### Delete a user
@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"],
)
def delete_user():
    pass


## Tweets

### Get all tweets
@app.get(
    path="/tweets/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Get all tweets",
    tags=["Tweets"],
)
def get_tweets():
    pass


### Get a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Get a tweet",
    tags=["Tweets"],
)
def get_tweet():
    pass

### Create a tweet
@app.post(
    path="/tweets/",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Create a tweet",
    tags=["Tweets"],
)
def create_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"],
)
def update_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"],
)
def delete_tweet():
    pass
