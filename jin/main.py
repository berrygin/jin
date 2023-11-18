import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.wsgi import WSGIMiddleware
from app1 import app as dashboard1
from app2 import app as dashboard2
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import redis

# Define the FastAPI server
app = FastAPI()
# Mount the Dash app as a sub-application in the FastAPI server
app.mount("/dashboard1", WSGIMiddleware(dashboard1.server))
app.mount("/dashboard2", WSGIMiddleware(dashboard2.server))
app.mount(path='/static', app=StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

# Define the main API endpoint
# @app.get("/")
# def index(request: Request):
#     script = '<div>hello</div>'
#     return 'hello world'
#     # return templates.TemplateResponse("page.html", {"request": request, "script": script})

@app.get("/")
async def redis_get(key: str):
    rc = redis.Redis(db=0, decode_responses=True)
    json_str = rc.get(key)# .decode()
    return json_str

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
