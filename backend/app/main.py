"""FastAPI application."""
from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
from furl import furl

from app.api.v1.api import api_router
from app.scheduling import scheduler, SchedulerMiddleware
from fastapi.middleware import Middleware

middleware = [Middleware(SchedulerMiddleware, scheduler=scheduler)]
app = FastAPI(middleware=middleware)


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
