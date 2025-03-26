from fastapi import APIRouter

from src.presentation.api.v1.endpoints.user import router as user_router

router = APIRouter(prefix="/api/v1")
router.include_router(user_router)
