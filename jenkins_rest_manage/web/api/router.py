from fastapi.routing import APIRouter

from jenkins_rest_manage.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
