"""FastAPI application."""
from contextlib import asynccontextmanager

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from furl import furl

from app.api.v1.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context."""
    app.state.scheduler = AsyncIOScheduler()
    try:
        app.state.scheduler.start()
        yield
    finally:
        app.state.scheduler.shutdown()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8100"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

