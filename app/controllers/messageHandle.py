from typing import Dict
from app import Utils

jsonPath = 'replyMap.json'


def getReply(content: str) -> Dict:
    replyJson = Utils.loadJson(jsonPath)

    elementSet = set(replyJson.keys())  # 将列表转换为集合
    containedElements = []
    for element in elementSet:  # 遍历集合，避免重复检查
        if element in content:
            containedElements.append(element)

    answer = ""

    for element in containedElements:
        answer += replyJson.get(element)

    return {
        "type": "text",
        "content": answer
    }
