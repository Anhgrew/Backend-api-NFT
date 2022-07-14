from fastapi import APIRouter, Body, UploadFile, File
from starlette.requests import Request
import requests
from services.upload import upload_file
from db.models.user import UserHistory
from datetime import datetime
import json
from core.config import settings

router = APIRouter()


@router.get("/{user_id}/history")
async def get_user_history(user_id: str):
    all_history = (
        await UserHistory.find(UserHistory.user_id == user_id)
        .sort(UserHistory.created_at)
        .to_list()
    )
    return all_history


@router.post("/{user_id}/search")
async def get_image_search(user_id: str, data: UploadFile = File(...)):
    # handle image by s3
    buffer = await data.read()
    filename = data.filename
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    search_img_url = await upload_file(data=buffer, filename=filename)
    # get search result

    res = requests.request("POST", settings.SEARCH_API, headers=headers, data=buffer)
    result = res.json()["result"]
    print(type(result))

    new_user_history = UserHistory(
        user_id=user_id,
        search_img_url=search_img_url,
        result=result,
        created_at=datetime.utcnow(),
    )
    user_history_record = await new_user_history.save()
    return new_user_history
