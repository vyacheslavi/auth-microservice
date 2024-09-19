from fastapi.routing import APIRouter

from .handlers.auth import router as auth_router


router = APIRouter()

router.include_router(auth_router)
