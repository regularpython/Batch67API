import json

from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Router, Response

app = ApiGatewayResolver()
user_router = Router()



@user_router.get("/get-details")
def get_user_details():
    uid = user_router.current_event.get('queryStringParameters', {}).get('uid')
    name = user_router.current_event.get('queryStringParameters', {}).get('name')
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "user details", "user_id": uid, "name": name})
    )


@user_router.get("/get-details")
def get_user_details():
    uid = user_router.current_event.get("queryStringParameters", {}).get("uid")
    name = user_router.current_event.get("queryStringParameters", {}).get("name")
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "user details", "user_id": uid, "name": name})
    )


@user_router.post("/create")
def create_user():
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "Create user"})
    )


@user_router.get("/get-user")
def get_single_user():
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "Single User Details"})
    )


@user_router.put("/update")
def update_user():
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "Update user details"})
    )


@user_router.delete("/delete/<user_id>/<name>")
def delete_user(user_id: str, name: str):
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "User Delete", "deleted user_id": user_id, "name": name})
    )
