# registry.py

from sqlalchemy.orm import registry

from src.orm.models.user_models import UserModel
from src.orm.tables.user_table import user_table

# Create a registry object
mapper_registry = registry()


def run_mappers():
    mapper_registry.map_imperatively(UserModel, user_table)
