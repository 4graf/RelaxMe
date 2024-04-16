api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(users_routes.router, prefix="/users", tags=["Users"])
