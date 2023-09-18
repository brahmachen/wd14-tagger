from fastapi import FastAPI
from tagger.api import on_app_started
import uvicorn

app = FastAPI()

on_app_started(None, app)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=7867, log_level="info")