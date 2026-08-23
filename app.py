from fastapi import FastAPI
from schemas import Message, UserSchema, UserPublic, UserDB, UserList
from http import HTTPStatus
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = []

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá FastAPI!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)  

    database.append(user_with_id)
    logger.info("Database: %s", database)
    return user_with_id

@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}

print(database)