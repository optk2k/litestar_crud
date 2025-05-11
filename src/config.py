from os import environ

from dotenv import load_dotenv
from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)

load_dotenv()


sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=f"postgresql+asyncpg://{environ["user"]}:{environ["password"]}@{environ["host"]}/{environ["database"]}",
    before_send_handler="autocommit",
    session_config=AsyncSessionConfig(expire_on_commit=False),
    create_all=True,
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)
