"""FastAPI application."""
from fastapi import FastAPI, Request, status
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from furl import furl

from app.api.v1.api import api_router
from app.repositories import ApSchedulerRepository
from app.scheduling import SchedulerMiddleware, scheduler
from app.services.schedule import service_get_schedules

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8100"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SchedulerMiddleware, scheduler=scheduler)

@app.on_event("startup")
async def startup_event():
    """Startup event.

    :return:
    """
    schedule_data_list: list[dict] = await run_in_threadpool(service_get_schedules)
    ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
    await ap_repo.create_multiple(schedule_data_list)


@app.get("/", include_in_schema=False)
def redirect_to_autodocs(request: Request) -> RedirectResponse:
    """Home Page of the application.

    :param Request request:
    :return: RedirectResponse
    """
    furl_item: furl = furl(request.base_url)
    furl_item.path /= app.docs_url
    return RedirectResponse(
        furl_item.url, status_code=status.HTTP_301_MOVED_PERMANENTLY
    )


app.include_router(api_router, prefix="/v1")
