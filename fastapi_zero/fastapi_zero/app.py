from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fastapi_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)  # filtra os dados privados
def create_user(user: UserSchema):
    user_with_id = UserDB(
        **user.model_dump(),  # transforma o modelo em um dicionário de volta (substitui a inserção manual)
        id=len(database) + 1,
    )

    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def get_usuarios():
    return {'users': database}


@app.get('/users/{id_user}', status_code=HTTPStatus.OK, response_model=UserPublic)
def get_usuario(id_user: int):
    if id_user > len(database) or id_user < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return database[id_user - 1]


@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return database.pop(user_id - 1)
