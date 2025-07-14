from fastapi import FastAPI
from . import models
from .database import engine
from .routes import wheel_spec_routes

app = FastAPI()

# Create tables in DB
models.Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(wheel_spec_routes.router)
