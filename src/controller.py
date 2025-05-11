from typing import Any

from advanced_alchemy.exceptions import NotFoundError
from advanced_alchemy.extensions.litestar.providers import create_service_dependencies
from advanced_alchemy.filters import LimitOffset
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import OffsetPagination, SQLAlchemyAsyncRepositoryService
from litestar import Controller, Response, delete, get, post, put
from litestar.exceptions import NotFoundException

from schemas import UserCreateSchema, UserGetSchema, UserModel, UserUpdateSchema


class UserService(SQLAlchemyAsyncRepositoryService[UserModel]):
    """User service."""

    class Repo(SQLAlchemyAsyncRepository[UserModel]):
        """User repository."""

        model_type = UserModel

    repository_type = Repo


def user_is_not_found(
    request: Any, exc: NotFoundException
) -> Response[dict[str, int | str]]:
    return Response(
        content={"status_code": 404, "detail": "User is not found!"},
        status_code=404,
    )


class UserController(Controller):
    """User CRUD endpoints."""

    path = "/user"
    dependencies = create_service_dependencies(UserService, key="user_service")
    tags = ["Users"]

    @get()
    async def users(
        self, user_service: UserService, offset: int = 0, limit: int = 10
    ) -> OffsetPagination[UserGetSchema]:
        """List all users."""
        results, total = await user_service.list_and_count(
            LimitOffset(offset=offset, limit=limit)
        )
        return user_service.to_schema(results, total, schema_type=UserGetSchema)

    @post()
    async def user_create(
        self,
        user_service: UserService,
        data: UserCreateSchema,
    ) -> UserGetSchema:
        """Create a new user."""
        obj: UserModel = await user_service.create(data)  # type: ignore
        return user_service.to_schema(data=obj, schema_type=UserGetSchema)

    @get(path="/{user_id:int}", exception_handlers={NotFoundError: user_is_not_found})
    async def user_get(
        self,
        user_service: UserService,
        user_id: int,
    ) -> UserGetSchema:
        """Get a user."""
        obj = await user_service.get(user_id)
        return user_service.to_schema(data=obj, schema_type=UserGetSchema)

    @put(path="/{user_id:int}", exception_handlers={NotFoundError: user_is_not_found})
    async def user_update(
        self,
        user_service: UserService,
        user_id: int,
        data: UserUpdateSchema,
    ) -> UserGetSchema:
        """Update an user."""
        obj: UserModel = await user_service.update(data=data, item_id=user_id)  # type: ignore
        return user_service.to_schema(obj, schema_type=UserGetSchema)

    @delete(
        path="/{user_id:int}", exception_handlers={NotFoundError: user_is_not_found}
    )
    async def user_delete(
        self,
        user_service: UserService,
        user_id: int,
    ) -> None:
        """Delete a user."""
        await user_service.delete(user_id)
