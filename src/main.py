from fastapi import FastAPI

from src.presentation.api.v1.router import router


def create_app():
    app = FastAPI()
    app.include_router(router)

    return app


app = create_app()


@app.get("/")
async def hello():
    return {"message": "hello there"}
