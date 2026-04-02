from fastapi import FastAPI
from app.database import Base, engine
from app.routes import record_routes
from app.routes import auth_routes
from app.routes import user_routes

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(record_routes.router, prefix="/records", tags=["Records"])
@app.get("/")
def root():
    return {"message": "Finance Backend is Running 🚀"}