from fastapi import FastAPI
from schemas import Message, UserSchema, UserPublic
from http import HTTPStatus
app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá FastAPI!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user