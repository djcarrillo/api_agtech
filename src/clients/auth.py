import logging
import requests

from fastapi import status, Header, HTTPException
from config import settings

settings = settings.Setting()

logger = logging.getLogger(__name__)


def validate_jwt(x_auth_login_token: str = Header(...)):

    #url = settings.URL_AUTH_API_LB + f"/auth/user"

    if (
        #requests.get(url=url, headers={"x-token": f"{x_auth_login_token}"}).status_code
        #!= status.HTTP_200_OK
        x_auth_login_token != settings.x_auth_login_token
    ):
        logger.error("X-Token header invalid")
        raise HTTPException(
            status_code=401, detail="Error: x-auth-login-token header invalid"
        )
