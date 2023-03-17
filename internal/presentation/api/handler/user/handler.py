import logging

from dependency_injector.wiring import Provide, inject
from flask import request
from flask_api import status
from flask_restx import Resource

# from flask_restx import reqparse
from psycopg2.errors import NotNullViolation, UniqueViolation
from sqlalchemy.exc import IntegrityError

from internal.application.service.user.service import Service as UserService
from internal.core.domain.entity.user import User as DomainUser
from internal.di.di import AppContainer
from internal.presentation.api.handler.user import (
    creatable_user_model,
    error_model,
    updatable_user_model,
    user_collection_model,
    user_model,
    user_namespace,
)
from internal.presentation.api.presentable_entity.error import Error
from internal.presentation.api.presentable_entity.user import User

logger = logging.getLogger(__name__)

# parser = reqparse.RequestParser()
# parser.add_argument("var1", type=str, help="variable 1")
# parser.add_argument("var2", type=str, help="variable 2")


@user_namespace.route("/user")
class UserResource(Resource):
    @inject
    def __init__(
        self,
        api=None,
        service: UserService = Provide[AppContainer.service.user_service],
        *args,
        **kwargs
    ):
        self.service = service
        super().__init__(api, *args, **kwargs)

    # @user_namespace.doc("create_user", parser=parser)
    @user_namespace.doc("create_user")
    @user_namespace.expect(creatable_user_model)
    @user_namespace.response(
        code=status.HTTP_201_CREATED, model=user_model, description="Created"
    )
    @user_namespace.response(
        code=status.HTTP_400_BAD_REQUEST,
        model=error_model,
        description="Bad Request",
    )
    # @user_namespace.response(
    #     code=status.HTTP_401_UNAUTHORIZED,
    #     model=error_model,
    #     description="Unauthorized",
    # )
    # @user_namespace.response(
    #     code=status.HTTP_404_NOT_FOUND,
    #     model=error_model,
    #     description="Not Found",
    # )
    @user_namespace.response(
        code=status.HTTP_409_CONFLICT,
        model=error_model,
        description="Conflict",
    )
    @user_namespace.response(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        model=error_model,
        description="Internal Server Error",
    )
    def post(self):
        data = request.json
        if data:
            username = data.get("username")
            domain_user = DomainUser(username=username)
            try:
                returned_domain_user = self.service.create(user=domain_user)
                return (
                    User.from_domain(domain=returned_domain_user).to_json(),
                    status.HTTP_201_CREATED,
                )
            except IntegrityError as ex:
                if isinstance(ex.orig, NotNullViolation):
                    logger.error("%s", ex)
                    text = "Bad Request"
                    return (
                        Error(text=text).to_json(),
                        status.HTTP_400_BAD_REQUEST,
                    )

                if isinstance(ex.orig, UniqueViolation):
                    logger.error("%s", ex)
                    text = "Conflict"
                    return (
                        Error(text=text).to_json(),
                        status.HTTP_409_CONFLICT,
                    )
            except (Exception,) as ex:
                logger.error("%s", ex)
                text = "Internal Server Error"
                return (
                    Error(text=text).to_json(),
                    status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        text = "Bad Request"
        return Error(text=text).to_json(), status.HTTP_400_BAD_REQUEST


@user_namespace.route("/users")
class UserCollectionResource(Resource):
    @inject
    def __init__(
        self,
        api=None,
        service: UserService = Provide[AppContainer.service.user_service],
        *args,
        **kwargs
    ):
        self.service = service
        super().__init__(api, *args, **kwargs)

    @user_namespace.doc("get_all_users")
    @user_namespace.response(
        code=status.HTTP_200_OK, model=user_collection_model, description="OK"
    )
    @user_namespace.response(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        model=error_model,
        description="Internal Server Error",
    )
    def get(self):
        try:
            returned_domain_users = self.service.get_all()
            users = []
            for returned_domain_user in returned_domain_users:
                users.append(User.from_domain(domain=returned_domain_user).to_json())
            return users, status.HTTP_200_OK
        except (Exception,) as ex:
            logger.error("%s", ex)
            text = "Internal Server Error"
            return (
                Error(text=text).to_json(),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@user_namespace.route("/users/<string:user_id>")
class UsersResource(Resource):
    @inject
    def __init__(
        self,
        api=None,
        service: UserService = Provide[AppContainer.service.user_service],
        *args,
        **kwargs
    ):
        self.service = service
        super().__init__(api, *args, **kwargs)

    @user_namespace.doc("get_user_by_id")
    @user_namespace.response(
        code=status.HTTP_200_OK, model=user_model, description="OK"
    )
    @user_namespace.response(
        code=status.HTTP_400_BAD_REQUEST,
        model=error_model,
        description="Bad Request",
    )
    @user_namespace.response(
        code=status.HTTP_404_NOT_FOUND,
        model=error_model,
        description="Not Found",
    )
    @user_namespace.response(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        model=error_model,
        description="Internal Server Error",
    )
    def get(self, user_id):
        try:
            user = self.service.get_by_id(id=user_id)
            if not user:
                logger.error("Not Found")
                text = "Not Found"
                return (
                    Error(text=text).to_json(),
                    status.HTTP_404_NOT_FOUND,
                )
            return User.from_domain(domain=user).to_json()
        except ValueError as ex:
            logger.error("%s", ex)
            text = "Bad Request"
            return (
                Error(text=text).to_json(),
                status.HTTP_400_BAD_REQUEST,
            )
        except (Exception,) as ex:
            logger.error("%s", ex.orig)
            text = "Internal Server Error"
            return (
                Error(text=text).to_json(),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @user_namespace.doc("update_user")
    @user_namespace.expect(updatable_user_model)
    @user_namespace.response(
        code=status.HTTP_200_OK, model=user_model, description="OK"
    )
    @user_namespace.response(
        code=status.HTTP_400_BAD_REQUEST,
        model=error_model,
        description="Bad Request",
    )
    @user_namespace.response(
        code=status.HTTP_404_NOT_FOUND,
        model=error_model,
        description="Not Found",
    )
    @user_namespace.response(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        model=error_model,
        description="Internal Server Error",
    )
    def put(self, user_id):
        data = request.json
        if data:
            username = data.get("username")
            domain_user = DomainUser(id=user_id, username=username)
            try:
                updated_domain_user = self.service.update(id=user_id, user=domain_user)
                if not updated_domain_user:
                    logger.error("Not Found")
                    text = "Not Found"
                    return (
                        Error(text=text).to_json(),
                        status.HTTP_404_NOT_FOUND,
                    )
                return (
                    User.from_domain(domain=updated_domain_user).to_json(),
                    status.HTTP_200_OK,
                )
            except IntegrityError as ex:
                if isinstance(ex.orig, NotNullViolation):
                    logger.error("%s", ex)
                    text = "Bad Request"
                    return (
                        Error(text=text).to_json(),
                        status.HTTP_400_BAD_REQUEST,
                    )
            except ValueError as ex:
                logger.error("%s", ex)
                text = "Bad Request"
                return (
                    Error(text=text).to_json(),
                    status.HTTP_400_BAD_REQUEST,
                )
            except (Exception,) as ex:
                logger.error("%s", ex)
                text = "Internal Server Error"
                return (
                    Error(text=text).to_json(),
                    status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        text = "Bad Request"
        return Error(text=text).to_json(), status.HTTP_400_BAD_REQUEST

    @user_namespace.doc("delete_user")
    @user_namespace.response(
        code=status.HTTP_200_OK, model=user_model, description="OK"
    )
    @user_namespace.response(
        code=status.HTTP_404_NOT_FOUND,
        model=error_model,
        description="Not Found",
    )
    @user_namespace.response(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        model=error_model,
        description="Internal Server Error",
    )
    def delete(self, user_id):
        try:
            user = self.service.delete(id=user_id)
            if not user:
                logger.error("Not Found")
                text = "Not Found"
                return (
                    Error(text=text).to_json(),
                    status.HTTP_404_NOT_FOUND,
                )
            return User.from_domain(domain=user).to_json()
        except ValueError as ex:
            logger.error("%s", ex)
            text = "Bad Request"
            return (
                Error(text=text).to_json(),
                status.HTTP_400_BAD_REQUEST,
            )
        except (Exception,) as ex:
            logger.error("%s", ex.orig)
            text = "Internal Server Error"
            return (
                Error(text=text).to_json(),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
