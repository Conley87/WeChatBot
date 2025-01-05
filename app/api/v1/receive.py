import json
from typing import Dict

from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from app.controllers import messageHandle
from app.schemas.resp import Success
from app.logs import logger
from app import config

router = APIRouter()


@router.post('/receive')
async def receive(type: str = Form(...),
                  content: str = Form(...),
                  source: str = Form(...),
                  isMentioned: str = Form(...),
                  isMsgFromSelf: str = Form(...)):
    sourceDict: Dict = json.loads(source)

    if not config.REPLYMODE or isMentioned == '1':
        match type:
            case 'text':
                logger.debug(f"{sourceDict['from']['id']}--{isMentioned}: {content}")

                reply = messageHandle.getReply(content)

                return Success(code=200, msg=True, data=reply)

            case 'urlLink' | 'file' | 'friendship':
                logger.debug(f"{type} : {sourceDict}")
            case 'system_event_login' | 'system_event_logout' | 'system_event_push_notify':
                logger.info(f"{type}")
            case 'system_event_error':
                logger.error(f"{type}: {sourceDict}")
            case _:
                logger.info(f"未实现的消息类型(unknown): {content} {sourceDict}")

    return JSONResponse(status_code=200, content=None)


@router.get('/test')
async def test():
    logger.info("你好")
    return JSONResponse(content={"status": "success", "data": config.REPLYMODE})
