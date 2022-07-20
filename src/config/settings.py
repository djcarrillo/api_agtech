import os


class Setting:

    VERSION = "1.0.0"
    ENVIRONMENT = "DEV" if os.getenv("MACHINE", 'DEV') == "DEV" else "PROD"
    ROOT_PATH = "" if ENVIRONMENT == "DEV" else "/empowerment"
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "['*']")
    ALLOW_CREDENTIALS = os.getenv("ALLOW_CREDENTIALS", True)
    ALLOW_METHODS = os.getenv("ALLOW_METHODS", "['*']")
    ALLOW_HEADERS = os.getenv("ALLOW_HEADERS", "['*']")

    USER_AWS = os.getenv('user')
    ACCESS_KEY_ID_AWS = os.getenv('access_key_id')
    SECRET_ACCESS_KEY_AWS = os.getenv('secret_access_key')
    PASSWORD_AWS = os.getenv('password')

    polygon_auth = os.getenv('polygon_auth')
    x_auth_login_token = os.getenv('jwt')
    user_table=os.getenv('dynamo_table')
