from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd


app = FastAPI()
app.mount(path='/static', app=StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

URL = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv" # 世界各国別データ（ECDE オープンデータ）
df = pd.read_csv(URL).iloc[:20, :]
df.drop(df.columns[[11]], axis=1, inplace=True)

@app.get("/")
# async def app_page(request: Request):
def front_page(request: Request):
    html = df.to_html(index=False)
    return templates.TemplateResponse("page.html", {"request": request, "html": html})
