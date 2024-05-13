from fastapi import APIRouter

from microservices.backend.api.v1 import stress_routes, user_routes, eeg_routes

api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(stress_routes.router, prefix="/stress", tags=["Stress"])
api_v1_router.include_router(user_routes.router, prefix="/user", tags=["User"])
api_v1_router.include_router(eeg_routes.router, prefix="/eeg", tags=["EEG"])

api_routers = [api_v1_router]
