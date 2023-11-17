### 起動

```shell
cd jin
uvicorn main:app --reload
```
o http://127.0.0.1:8000/  
x localhost:8000

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```