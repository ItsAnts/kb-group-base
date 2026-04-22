from typing import Optional
from litestar import Litestar, Request, get

COUNT: int = 0


@get("/")
async def index() -> str:
    global COUNT
    COUNT += 1
    if COUNT % 2 == 0:
        return "КАКОЙ ТЫ ЧЕТКИЙ"
    else:
        return "КАКОЙ ТЫ НЕ ЧЕТКИЙ"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


@get(path="/me")
async def get_me(request: Request) -> Optional[dict[str, str | int | dict]]:
    if request.client is None:
        return None
    host = request.client.host
    port = request.client.port
    header = dict(request.headers)
    return {"IP": host, "PORT": port, "HEADERS": header}


app = Litestar(route_handlers=[index, get_book, get_me])
