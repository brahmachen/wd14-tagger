from fastapi import FastAPI
from tagger.api import on_app_started

app = FastAPI()

on_app_started(None, app)