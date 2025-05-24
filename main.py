from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from src.controllers import mock_data_controller
from src.middlewares.firebase_auth_middleware import FirebaseAuthMiddleware
from src.services.firebase_admin_service import init_firebase

load_dotenv()

app = FastAPI()

init_firebase()

# Middleware Firebase Auth
app.add_middleware(FirebaseAuthMiddleware)

# Leer orígenes CORS desde entorno
raw_origins = os.getenv("CORS_ORIGINS", "")
origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(mock_data_controller.router, prefix="/data", tags=["chargers"])
