from typing import Optional, Any

from fastapi.responses import JSONResponse


class Success(JSONResponse):
    def __init__(
            self,
            code: int = 200,
            msg: bool = True,
            data: Optional[Any] = None
    ):
        content = {"success": msg, "data": data}
        super().__init__(status_code=code, content=content)
