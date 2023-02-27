import logging

from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify, request
from flask_api import status

from internal.application.service.user.service import Service as UserService
from internal.core.domain.entity.user import User as DomainUser
from internal.di.di import AppContainer
from internal.presentation.api.entity.user import User

logger = logging.getLogger(__name__)

blueprint = Blueprint("user_route", __name__)


@blueprint.route("/user", methods=["POST"])
@inject
def create_user(
    service: UserService = Provide[AppContainer.service.user_service],
):
    if request.json:
        username = request.json["username"]
        domain_user = DomainUser(username=username)
        try:
            returned_domain_user = service.create(domain_user)
            user = User.from_domain(domain=returned_domain_user)
            return jsonify(user), status.HTTP_201_CREATED
        except (Exception,) as ex:
            logger.error("%s", ex)
            return jsonify({"error": ex}), status.HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({"error": "Bad request"}), status.HTTP_400_BAD_REQUEST


@blueprint.route("/users", methods=["GET"])
@inject
def get_all_users(
    service: UserService = Provide[AppContainer.service.user_service],
):
    try:
        returned_domain_users = service.get_all()
        users = []
        for returned_domain_user in returned_domain_users:
            users.append(User.from_domain(domain=returned_domain_user))
        return jsonify(users), status.HTTP_200_OK
    except (Exception,) as ex:
        logger.error("%s", ex)
        return jsonify({"error": ex}), status.HTTP_500_INTERNAL_SERVER_ERROR
