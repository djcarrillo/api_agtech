from typing import Dict, List
from psycopg2 import Timestamp
from pydantic import BaseModel


class FavoriteCompanies(BaseModel):
    name: str
    created_at_: Timestamp


class DiscardedCompanies(BaseModel):
    name: str
    created_at_: Timestamp


class UserTrade(BaseModel):
    user_id: str
    created_at: Timestamp
