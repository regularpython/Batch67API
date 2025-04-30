import json
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Response

from src.routers.user_router import user_router

app = ApiGatewayResolver()


app.include_router(user_router)


def lambda_handler(event, context):
    return app.resolve(event, context)



    # endpoint = event['path']


    # if endpoint == "/user/get-details":
    #     uid = event.get('queryStringParameters', {}).get('uid')
    #     name = event.get('queryStringParameters', {}).get('name')
    #     # Write your business logic here
    #     return {
    #         "statusCode": 200,
    #         "body": json.dumps({"message": "user details", 'user_id': uid, 'name': name}),
    #     }
    # elif endpoint == "/user/create":
    #     # Write your business logic here
    #     return {
    #         "statusCode": 200,
    #         "body": json.dumps({"message": "Create user"}),
    #     }
    # elif endpoint == "/user/get-user":
    #     # Write your business logic here
    #     return {
    #         "statusCode": 200,
    #         "body": json.dumps({"message": "Single User Details"}),
    #     }
    # elif endpoint == "/user/update":
    #     # Write your business logic here
    #     return {
    #         "statusCode": 200,
    #         "body": json.dumps({"message": "Update user details"}),
    #     }
    # elif endpoint.startswith("/user/delete/"):
    #     # Write your business logic here
    #     user_id = event.get('pathParameters', {}).get('user_id')
    #     name = event.get('pathParameters', {}).get('name')
    #     return {
    #         "statusCode": 200,
    #         "body": json.dumps({"message": "User Delete", 'deleted user_id': user_id, 'name': name}),
    #     }
    #
    # else:
    #     return {
    #         "statusCode": 200,
    #         "body": json.dumps({"message": "Service not found"}),
    #     }
