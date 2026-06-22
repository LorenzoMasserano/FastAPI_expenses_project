from typing import NoReturn
from fastapi import HTTPException, status

def raise_server_error() -> NoReturn:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=[
            {
                "type": "Server Error", 
                "msg": "Something goes wrong",
            }
        ]
    )
