import json

from worker.sql      import close_connection
from worker.errors   import NotFoundException
from worker.crawling import check_user_graduated



def lambda_handler(event, context):
    try:
        if check_user_graduated(user_id=event['id'], password=event['password']):
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "data": "",
                    "message": ""
                })
            }

        else:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "data": "",
                    "message": "UNGRADUATED"
                })
            }

    except NotFoundException:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "data": "",
                "message": "NOT_FOUND"
            })            
        }

    except Exception as error:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "data": "",
                "message": error
            })
        }
    
    finally:
        close_connection()