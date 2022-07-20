import json
import logging
import requests
import datetime
from typing import List
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Response, status, HTTPException
from utils import manage_datatime
from clients.auth import validate_jwt
from repositories import business_logical

price_company_router = APIRouter(
    prefix="/Agtech",
    dependencies=[Depends(validate_jwt)],
    responses={200: {"description": "Not found"}},
)


@price_company_router.get(
    "/test",
    tags=["Events"],
    status_code=status.HTTP_200_OK,
    summary="endpoint for test server",
)
def test():
    return "Un exito"


@price_company_router.get(
    "/available_symbols",
    status_code=status.HTTP_200_OK,
    summary="endpoint for get available symbols",
)
def symbols():
    try:
        symbols = business_logical.available_companies()
        return {
            'request_date': manage_datatime.now(),
            'symbols': symbols
        }
    except HTTPException as e:
        logging.error(f" request error {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content={"message": e.detail},
        )


@price_company_router.get(
    "/price_symbol",
    status_code=status.HTTP_200_OK,
    summary="endpoint for get price symbol"
)
def price_symbol(symbols: str, date: str, adjusted: str):
    try:
        price = business_logical.price_open_close(stocksTicker=symbols, date=date, adjusted=adjusted)
        return {
            'request_date': manage_datatime.now(),
            'symbol_price': price
        }
    except HTTPException as e:
        logging.error(f" request error {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content={"message": e.detail},
        )


@price_company_router.post(
    "/created_user",
    status_code=status.HTTP_200_OK,
    summary="endpoint for created new users"
)
def created_user(id: str,
                 favorite_companies: List,
                 discarded_companies: List, ):
    try:
        created_user = business_logical.created_user(user_id=id,
                                                     favorite_companies=favorite_companies,
                                                     discarded_companies=discarded_companies)
        result = {'status': created_user.get('status'), 'user_id': created_user.get('user_id')}
        return json.dumps(result)
    except HTTPException as e:
        logging.error(f" request error {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content={"message": e.detail},
        )


@price_company_router.post(
    "/send_favorite_companies",
    status_code=status.HTTP_200_OK,
    summary="endpoint for push favorite companies"
)
def send_companies_tracker(id: str,
                           favorite_companies: List):
    try:

        send_tracker = business_logical.companies_tracker(
            user_id=id, favorite_companies=favorite_companies)

        result = {'status': send_tracker.get('status'), 'user_id': send_tracker.get('user_id')}
        return json.dumps(result)
    except HTTPException as e:
        logging.error(f" request error {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content={"message": e.detail},
        )


@price_company_router.get(
    "/pull_price_companies",
    status_code=status.HTTP_200_OK,
    summary="endpoint for pull price favorite companies, this endpoint no adjust the price"
)
def pull_price_favorite(id: str, date: str):
    try:
        companies_price = business_logical.get_price_favorite(user_id=id, date=date)
        return json.dumps(companies_price)
    except HTTPException as e:
        logging.error(f" request error {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content={"message": e.detail},
        )

@price_company_router.get(
    "/extract_all",
    status_code=status.HTTP_200_OK,
    summary="returns the price of the available companies"
)
async def pull_price_all(date: str):
    try:
        companies_price = business_logical.get_price_all(user_id=id, date=date)
        return json.dumps(companies_price)
    except HTTPException as e:
        logging.error(f" request error {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content={"message": e.detail},
        )
# Save Symbols
# Consultar Symbols
# extraer el precio de cierre
