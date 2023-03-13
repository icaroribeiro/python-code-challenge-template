import logging

from dependency_injector.wiring import Provide, inject
from flask_api import status
from flask_restx import Resource, reqparse

from internal.application.service.user.service import Service as UserService
from internal.core.domain.entity.user import User as DomainUser
from internal.di.di import AppContainer
from internal.presentation.api.entity.error import Error
from internal.presentation.api.entity.message import Message
from internal.presentation.api.entity.user import User
from internal.presentation.api.handler.user import (
    error_model,
    user_list_model,
    user_namespace,
)

logger = logging.getLogger(__name__)

parser = reqparse.RequestParser()
parser.add_argument("var1", type=str, help="variable 1")
parser.add_argument("var2", type=str, help="variable 2")


@user_namespace.route("/users")
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

    @user_namespace.doc("get_all_users")
    # @health_check_namespace.doc("api", security="ApiKeyAuth")
    @user_namespace.response(
        code=status.HTTP_200_OK, model=user_list_model, description="OK"
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
            text = "Internal server error"
            return (
                Error(text=text).to_json(),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# import logging
#
# from dependency_injector.wiring import Provide, inject
# from flask import Blueprint, jsonify, request
# from flask_api import status
#
# from internal.application.service.user.service import Service as UserService
# from internal.core.domain.entity.user import User as DomainUser
# from internal.di.di import AppContainer
# from internal.presentation.api.entity.user import User
#
# logger = logging.getLogger(__name__)
#
# blueprint = Blueprint("user_route", __name__)
#
#
# @blueprint.route("/user", methods=["POST"])
# @inject
# def create_user(
#     service: UserService = Provide[AppContainer.service.user_service],
# ):
#     if request.json:
#         username = request.json["username"]
#         domain_user = DomainUser(username=username)
#         try:
#             returned_domain_user = service.create(domain_user)
#   1          user = User.from_domain(domain=returned_domain_user)
#             return jsonify(user), status.HTTP_201_CREATED
#         except (Exception,) as ex:
#             logger.error("%s", ex)
#             return (
#                 jsonify({"error": "Internal server error"}),
#                 status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
#
#     return jsonify({"error": "Bad request"}), status.HTTP_400_BAD_REQUEST
#
#
# @blueprint.route("/users", methods=["GET"])
# @inject
# def get_all_users(
#     service: UserService = Provide[AppContainer.service.user_service],
# ):
#     try:
#         returned_domain_users = service.get_all()
#         users = []
#         for returned_domain_user in returned_domain_users:
#             users.append(User.from_domain(domain=returned_domain_user))
#         return jsonify(users), status.HTTP_200_OK
#     except (Exception,) as ex:
#         logger.error("%s", ex)
#         return (
#             jsonify({"error": "Internal server error"}),
#             status.HTTP_500_INTERNAL_SERVER_ERROR,
#         )
#
#
# @blueprint.route("/users/<id>", methods=["GET"])
# @inject
# def get_user_by_id(
#     id,
#     service: UserService = Provide[AppContainer.service.user_service],
# ):
#     try:
#         returned_domain_user = service.get_by_id(id=id)
#         if returned_domain_user:
#             return (
#                 jsonify(User.from_domain(domain=returned_domain_user)),
#                 status.HTTP_200_OK,
#             )
#
#         return jsonify({"error": "Not found"}), status.HTTP_404_NOT_FOUND
#     except (Exception,) as ex:
#         logger.error("%s", ex)
#         return (
#             jsonify({"error": "Internal server error"}),
#             status.HTTP_500_INTERNAL_SERVER_ERROR,
#         )
#
#
# @blueprint.route("/users/<id>", methods=["PUT"])
# @inject
# def update_user(
#     id,
#     service: UserService = Provide[AppContainer.service.user_service],
# ):
#     if request.json:
#         username = request.json["username"]
#         domain_user = DomainUser(username=username)
#         try:
#             returned_domain_user = service.update(id=id, user=domain_user)
#             if returned_domain_user:
#                 user = User.from_domain(domain=returned_domain_user)
#                 return jsonify(user), status.HTTP_200_OK
#
#             return jsonify({"error": "Not found"}), status.HTTP_404_NOT_FOUND
#         except (Exception,) as ex:
#             logger.error("%s", ex)
#             return (
#                 jsonify({"error": "Internal server error"}),
#                 status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
#
#     return jsonify({"error": "Bad request"}), status.HTTP_400_BAD_REQUEST
#
#
# @blueprint.route("/users/<id>", methods=["DELETE"])
# @inject
# def delete_user(
#     id,
#     service: UserService = Provide[AppContainer.service.user_service],
# ):
#     try:
#         returned_domain_user = service.delete(id=id)
#         if returned_domain_user:
#             user = User.from_domain(domain=returned_domain_user)
#             return jsonify(user), status.HTTP_200_OK
#
#         return jsonify({"error": "Not found"}), status.HTTP_404_NOT_FOUND
#     except (Exception,) as ex:
#         logger.error("%s", ex)
#         return jsonify({"error": ex}), status.HTTP_500_INTERNAL_SERVER_ERROR
