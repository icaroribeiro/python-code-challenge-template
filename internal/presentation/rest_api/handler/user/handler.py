from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify, request

from flask_api import status
from internal.application.service.user.service import (
    Service as UserService,
)
from internal.core.domain.entity.user import User as DomainUser
from internal.di.di import AppContainer
from internal.presentation.rest_api.entity.user import User

blueprint = Blueprint("user_route", __name__)


@blueprint.route("/user", methods=["POST"])
@inject
def create_user(
    service: UserService = Provide[AppContainer.service.user_service],
):
    if request.json:
        username = request.json['username']
        domain_user = DomainUser(username=username)
        try:
            returned_domain_user = service.create(domain_user)
            user = User.from_domain(domain=returned_domain_user)
            return jsonify(user), status.HTTP_200_OK
        except (Exception,):
            return jsonify({"error": "Bad request"}), status.HTTP_400_BAD_REQUEST

    return jsonify({"error": "Bad request"}), status.HTTP_400_BAD_REQUEST
