from fastapi import FastAPI

from roadmap_ai.routes.roadmap import router

app = FastAPI()
app.include_router(router)
