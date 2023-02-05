from fastapi import APIRouter
from injector import Injector
from pydantic import BaseModel
from src.app.usecases.impl.call_myaccessor import CallMyAccessor

injector = Injector()

router = APIRouter(
    prefix='/hoge_v1',
    tags=['hoge_v1']
)

class TestRequest(BaseModel):
    addValue: int

@router.post("/")
async def root(body: TestRequest):
    accessor = injector.get(CallMyAccessor)
    accessor.add(body.addValue)
    return {"result": accessor.get()}
