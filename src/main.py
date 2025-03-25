from fastapi import FastAPI


def create_app():
    app = FastAPI()

    return app


app = create_app()


@app.get("/")
async def hello():
    return {"message": "hello there"}
