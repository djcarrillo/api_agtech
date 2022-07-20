import datetime
import boto3
from boto3.dynamodb.conditions import Key
from utils.conect_dynamo import init_dynamo_db


def get_status_table(_table_name):
    try:
        dynamo_db = init_dynamo_db()
        table = dynamo_db.Table(_table_name)
        status_table = table.table_status
        return status_table
        # TODO Cerrar la conexion
    except Exception as ex:
        raise ex


def get_favorite_company(_table_name, _user_id):
    try:
        dynamo_db = init_dynamo_db()
        table = dynamo_db.Table(_table_name)
        favorite_companies = table.get_item(key={'user_id': _user_id})

        return favorite_companies
    except Exception as ex:
        raise ex


def get_discarded_companies(_table_name, _user_id):
    try:
        dynamo_db = init_dynamo_db()
        table = dynamo_db.Table(_table_name)
        discarded_companies = table.get_item(key={'user_id': _user_id})

        return discarded_companies
    except Exception as ex:
        raise ex


def create_user(_table_name, _user_id, _favorite_companies, _discarded_companies):
    try:
        dynamo_db = init_dynamo_db()
        table = dynamo_db.Table(_table_name)

        response = table.put_item(Item={
            'user_id': _user_id,
            'favorite_companies': _favorite_companies,
            'discarded_companies': _discarded_companies,
            'created_at': str(datetime.datetime.now())
        }
        )
        return response
    except Exception as ex:
        raise ex


def update_favorite_companies(_table_name, _user_id, _favorite_companies):
    try:
        dynamo_db = init_dynamo_db()
        table = dynamo_db.Table(_table_name)

        response = table.update_item(Key={'user_id': _user_id},
                                     UpdateExpression="set favorite_companies=:t1",
                                     ExpressionAttributeValues={':t1': _favorite_companies}
                                     )
        return response
    except Exception as ex:
        raise ex


def get_atribute(_table_name, _user_id, _atribute):
    try:
        dynamo_db = init_dynamo_db()
        table = dynamo_db.Table(_table_name)

        response = table.query(
            KeyConditionExpression = Key('user_id').eq(_user_id)
                               )
        return response
    except Exception as ex:
        raise ex


def update_discarded_companies(_table_name, _user_id, _discarded_companies):
    try:
        dynamo_db = init_dynamo_db()
        table = dynamo_db.Table(_table_name)

        response = table.update_item(Key={'user_id': _user_id},
                                     UpdateExpression="set _discarded_companies=:t1",
                                     ExpressionAttributeValues={':t1': _discarded_companies}
                                     )
    except Exception as ex:
        raise ex

# TODO implementar un update
# TODO implementar un create
# TODO implementar un delete
# TODO decorar los metodos de llamado a la BD
