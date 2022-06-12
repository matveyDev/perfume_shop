import uvicorn

from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles

from perfume.routes import router as perfume_routes
from user.routes import router as user_routes


app = FastAPI()
app.include_router(perfume_routes)
app.include_router(user_routes)
# app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
