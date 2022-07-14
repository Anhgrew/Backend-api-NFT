from typing import Dict, List, Union, Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel, Json


class UserHistory(Document):
    user_id: str
    search_img_url: str
    result: List
    created_at: datetime

    class Config:
        schema_extra = {
            "user": {
                "user_id": "1945100381d534d9e3b4ac618451ab",
                "search_img_url": "https://searchphotobucket.s3.ap-southeast-1.amazonaws.com/bitmoji.png",
                "result": [
                    "token0",
                    "token1",
                    "token2",
                    "token3",
                    "token4",
                    "token5",
                    "token6",
                    "token7",
                    "token8",
                    "token9",
                ],
                "created_at": "data time now",
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
