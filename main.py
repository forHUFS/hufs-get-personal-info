import json

from worker.sql                 import close_connection
from worker.crawling            import check_user_graduated

from selenium.common.exceptions import UnexpectedAlertPresentException


def lambda_handler(event, context):
    try:
        body    = json.loads(event['body'])
        checker = check_user_graduated(
            user_pk  = body['pk'],
            user_id  = body['id'],
            password = body['password']
        )
        
        if checker:
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

    except UnexpectedAlertPresentException:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "data": "",
                "message": "UNAUTHORIZED"
            })
        }

    except Exception as error:
        print(error)
        return {
            "statusCode": 500,
            "body": json.dumps({
                "data": "",
                "message": "SERVER_ERROR"
            })
        }
    
    finally:
        close_connection()