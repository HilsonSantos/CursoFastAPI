from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from app.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get(path="/", status_code=HTTPStatus.OK, response_model=Message)
async def root():
    return {"message": "Olá Mundo!"}


@app.post(
    path="/api/v1/users/",
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
async def create_user(user: UserSchema):
    user_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_id)
    return user_id


@app.get(
    path="/api/v1/users/", status_code=HTTPStatus.OK, response_model=UserList
)
async def list_users():
    return {"users": database}


@app.put(
    path="/api/v1/users/{user_id}", response_model=UserPublic
)
async def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )
    user = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user
    return user


@app.delete(path="/api/v1/users/{user_id}", response_model=Message)
async def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )
    del database[user_id - 1]
    return {"message": "User deleted"}
