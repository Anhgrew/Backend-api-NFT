import boto3
import uuid
from botocore.client import Config
from fastapi import UploadFile, File
from PIL import Image
import io
from core.config import settings

ACCESS_KEY_ID = "AKIA43LPGUCEQJN3WKB7"
SECRET_ACCESS_ID = "eM8Mp4pB8XtIizFYk9IPVGfDiDJYCy1/Pvwms/qc"
BUCKET_NAME = "searchphotobucket"


s3 = boto3.resource(
    "s3",
    aws_access_key_id=settings.ACCESS_KEY_ID,
    aws_secret_access_key=settings.SECRET_ACCESS_ID,
    config=Config(signature_version="s3v4"),
)


async def upload_file(data: bytes, filename: str):
    image = io.BytesIO(data)
    filename_s3 = str(uuid.uuid4()) + filename
    s3.Bucket(BUCKET_NAME).put_object(Key=filename_s3, Body=image)
    url = "https://searchphotobucket.s3.ap-southeast-1.amazonaws.com/" + filename_s3
    return url
