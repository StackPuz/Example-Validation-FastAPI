import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas.user import User

app = FastAPI()
@app.get("/")
async def index():
    return FileResponse("app/static/index.html")

@app.post("/submit")
async def submit(user: User):
    return user

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return await get_error(exc)

async def get_error(exc: Exception) -> JSONResponse:
    if isinstance(exc, RequestValidationError):
        errors = {}
        for error in exc.errors():
            field_name = error["loc"][-1]
            errors[field_name] = error["msg"]
        return JSONResponse(errors, 400)
    return exc

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")