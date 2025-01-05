import json
from typing import Dict


def loadJson(path) -> Dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
