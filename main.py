import json

from worker.sql                 import close_connection
from worker.crawling            import check_user_graduated

from selenium.common.exceptions import UnexpectedAlertPresentException


def lambda_handler(event, context):
    try:
        origin = event['headers']['origin']
        print(origin)
        if event['httpMethod'] == 'OPTIONS':
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
                    "Access-Control-Allow-Origin": origin,
                    "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS",
                    "Access-Control-Allow-Credentials": True
                },
                "body": json.dumps({
                    "data": "",
                    "message": ""
                })
            }
        
        body    = json.loads(event['body'])
        checker = check_user_graduated(
            user_pk  = body['pk'],
            user_id  = body['id'],
            password = body['password']
        )
        
        if checker:
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
                    "Access-Control-Allow-Origin": origin,
                    "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS",
                    "Access-Control-Allow-Credentials": True
                },
                "body": json.dumps({
                    "data": "",
                    "message": ""
                })
            }

        else:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
                    "Access-Control-Allow-Origin": origin,
                    "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS",
                    "Access-Control-Allow-Credentials": True
                },                
                "body": json.dumps({
                    "data": "",
                    "message": "UNGRADUATED"
                })
            }

    except UnexpectedAlertPresentException:
        return {
            "statusCode": 401,
            "headers": {
                "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
                "Access-Control-Allow-Origin": origin,
                "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS",
                "Access-Control-Allow-Credentials": True
            },             
            "body": json.dumps({
                "data": "",
                "message": "UNAUTHORIZED"
            })
        }

    except Exception as error:
        print(error)
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
                "Access-Control-Allow-Origin": origin,
                "Access-Control-Allow-Methods": "POST, PUT, GET, OPTIONS",
                "Access-Control-Allow-Credentials": True
            },             
            "body": json.dumps({
                "data": "",
                "message": "SERVER_ERROR"
            })
        }
    
    finally:
        close_connection()