entrar no shell para inicializar o fast api
    poetry shell
    fastapi dev fastapi_zero/app.py

ou
    poetry run fastapi dev fastapi_zero/app.py

inicializador:
    uvicorn fastapi_zero.app:app --host 0.0.0.0
ou
    task run
