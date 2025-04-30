import json

from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Router, Response

app = ApiGatewayResolver()
user_router = Router()



@user_router.get("/user/get-details")
def get_user_details():
    uid = user_router.current_event.get('queryStringParameters', {}).get('uid')
    name = user_router.current_event.get('queryStringParameters', {}).get('name')
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "user details", "user_id": uid, "name": name})
    )