from fastapi import FastAPI, Query, Cookie, Header
from starlette.responses import JSONResponse
from starlette.requests import Request

from models import Item


app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


@app.get("/")
async def read_root():
	return {"Welcome to": "the ROOT!"}


@app.post("/items/")
async def create_item(item: Item,
					  cookie: str = Cookie(None)):
	print("a cookie?", cookie)
	return item


@app.get("/items/{item_id}")
async def read_item(*, item_id: int,
					user_agent: str = Header(None),
					request: Request):
	cookies = request.cookies
	content = {
		"message": "Come to the dark side, we have cookies",
		"user-agent": user_agent,
		"cookies": cookies
	}
	response = JSONResponse(content=content)
	response.set_cookie(key="fakesession", value="fake-cookie-session-value")
	return response
