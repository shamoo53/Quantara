from fastapi import Form
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

# Mount static files and templates directory
templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    print("WROK!@#")
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit")
async def submit_form(token: str = Form(...), protocol: str = Form(...), multiplier: int = Form(...)):
    return {"token": token, "protocol": protocol, "multiplier": multiplier}