from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.core.task import create_start_app_handler, create_stop_app_handler
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.add_event_handler("startup", create_start_app_handler(app))
    # app.add_event_handler("shutdown", create_stop_app_handler(app))

app.include_router(api_router, prefix=settings.API_V1_STR)
