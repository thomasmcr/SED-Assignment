from urllib.parse import urlencode
from fastapi.responses import RedirectResponse
from starlette.requests import Request
from starlette.responses import JSONResponse

class AuthRedirect(Exception):
    def __init__(self, name: str = "AuthRedirect"):
        self.name = name

#Catches AuthRedirect and redirects to unauthorised page
async def handler(request: Request, exc: RuntimeError) -> JSONResponse:
    query_params = {"old_path": request.url.path}
    redirect_url = f"/unauthorised?{urlencode(query_params)}"
    return RedirectResponse(url=redirect_url)