from fastapi import APIRouter

from micro_services.backend.api.v1 import stress_routes

api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(stress_routes.router, prefix="/stress", tags=["Stress"])

api_routers = [api_v1_router]
