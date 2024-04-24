from fastapi import APIRouter

from microservices.stress_recognizer.api.v1 import stress_eeg_routes

api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(stress_eeg_routes.router, prefix="/stress_eeg", tags=["StressEEG"])

api_routers = [api_v1_router]
