from sqlalchemy import Table, Column, Integer, String, MetaData

# Define the metadata
metadata = MetaData()

# Define the users table
user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(45), nullable=True),
    Column("email", String(45), nullable=True),
    Column("age", Integer, nullable=True),
)
