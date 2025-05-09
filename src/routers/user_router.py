import json

from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Router, Response
from sqlalchemy import text

from src.orm.database import engine
from src.orm.models.user_models import UserModel
from src.orm.repositories.user_repository import UserRepository
from dataclasses import asdict
app = ApiGatewayResolver()
user_router = Router()


@user_router.get("/get-details")
def get_user_details():
    # Execute the query

    repo = UserRepository()
    result = repo.get_all_user()
    result = [asdict(user) for user in result]

    # Return as JSON
    return Response(
        status_code=200,
        content_type="application/json",
        headers={
            "Access-Control-Allow-Origin": "*",  # Allow requests from any origin
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        body=json.dumps({
            "message": "user details",
            "users": result
        })
    )


@user_router.post("/create")
def create_user():
    body = user_router.current_event.json_body
    name = body.get("name")
    email = body.get("email")
    age = body.get("age")
    # Create
    user = UserModel(
        name=name,
        age=age,
        email=email
    )
    repo = UserRepository()
    result = repo.create(user)
    result = asdict(result)
    if not name or not email or not age:
        return Response(
            status_code=400,
            content_type="application/json",
            headers={
                "Access-Control-Allow-Origin": "*",  # Allow requests from any origin
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "*"
            },
            body=json.dumps({"message": "Missing required fields"})
        )


    return Response(
        status_code=201,
        content_type="application/json",
        headers={
            "Access-Control-Allow-Origin": "*",  # Allow requests from any origin
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        body=json.dumps({"message": "User created successfully","user": result})
    )


@user_router.get("/get-user")
def get_single_user():
    # Get user id from query string paramete
    # Where condition
    repo = UserRepository()
    result = repo.get_single_user(1)
    result = asdict(result)
    print(result)

    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "Single User Details", "user": result})
    )


@user_router.put("/update")
def update_user():
    # Get the user details from json body
    # Create
    user = UserModel(
        id=3,
        name="siva kumar",
        age=20,
        email="siva@1234"
    )
    repo = UserRepository()
    result = repo.update(user)
    result = asdict(result)
    print(result)
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "Update user details", "result": result})
    )


@user_router.delete("/delete/<user_id>/<name>")
def delete_user(user_id: str, name: str):
    # Get the user id from path parameter
    # Delete
    repo = UserRepository()
    repo.delete_user(1)
    return Response(
        status_code=200,
        content_type="application/json",
        body=json.dumps({"message": "User Delete", "deleted user_id": user_id, "name": name})
    )
