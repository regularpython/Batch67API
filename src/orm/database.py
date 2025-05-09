# database.py

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.common.config import rds_access_protocol, rds_username, rds_password, rds_host, rds_port, rds_db_name


def get_db_connection():
    protocol = rds_access_protocol
    username = rds_username
    password = rds_password
    host = rds_host
    port = rds_port
    db_name = rds_db_name
    return f"{protocol}://{username}:{password}@{host}:{port}/{db_name}"

dialect = get_db_connection()

# Create an engine and initialize the database
engine = create_engine(dialect, pool_size=10, max_overflow=5, echo=True)  # Use appropriate database URL

#
# Set up the session factory
SESSION_FACTORY = sessionmaker(autocommit=False, autoflush=False, bind=engine)

