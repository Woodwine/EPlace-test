from fastapi import FastAPI
from beanie import init_beanie

from src.core.db import db

app = FastAPI(
    title='EPlace-test'
)


@app.on_event("startup")
async def init():
    await init_beanie(
        database=db.get_default_database(),
        document_models=[],
    )
