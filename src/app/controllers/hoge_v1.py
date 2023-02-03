from fastapi import APIRouter

router = APIRouter(
    prefix='/hoge_v1',
    tags=['hoge_v1']
)

@router.get("/")
async def root():

    return {"message": "hoge_v1"}
