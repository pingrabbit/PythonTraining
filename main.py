import fastapi
import uvicorn


print("Hello fastapi")

api = fastapi.FastAPI()

@api.get("/")
def index():
    return {"msg": "Hello from FastAPI", "another msg": ["Hello", "Momo"]}

uvicorn.run(api)