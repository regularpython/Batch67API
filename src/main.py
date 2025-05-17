
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Response, CORSConfig

from src.orm.orm_registry import run_mappers
from src.routers.user_router import user_router
run_mappers()
# app = ApiGatewayResolver()

cors_config = CORSConfig(allow_origin="*")
app = ApiGatewayResolver(cors=cors_config)

app.include_router(user_router, prefix='/user')


def lambda_handler(event, context):
    return app.resolve(event, context)
