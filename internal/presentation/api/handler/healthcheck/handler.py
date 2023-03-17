import logging

from dependency_injector.wiring import Provide, inject
from flask_api import status
from flask_restx import Resource

from internal.application.service.healthcheck.service import (
    Service as HealthCheckService,
)
from internal.di.di import AppContainer
from internal.presentation.api.handler.healthcheck import (
    error_model,
    health_check_namespace,
    message_model,
)
from internal.presentation.api.presentable_entity.error import Error
from internal.presentation.api.presentable_entity.message import Message

logger = logging.getLogger(__name__)


@health_check_namespace.route("/status")
class HealthCheckResource(Resource):
    @inject
    def __init__(
        self,
        api=None,
        service: HealthCheckService = Provide[AppContainer.service.healthcheck_service],
        *args,
        **kwargs
    ):
        self.service = service
        super().__init__(api, *args, **kwargs)

    @health_check_namespace.doc("get_status")
    # @health_check_namespace.doc("api", security="ApiKeyAuth")
    @health_check_namespace.response(
        code=status.HTTP_200_OK, model=message_model, description="OK"
    )
    @health_check_namespace.response(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        model=error_model,
        description="Internal Server Error",
    )
    def get(self):
        try:
            if not self.service.get_status():
                logger.error("the app is not ready to work as expected")
                text = "the app is not ready to work as expected"
                return (
                    Error(text=text).to_json(),
                    status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except (Exception,) as ex:
            logger.error("%s", ex)
            text = "Internal Server Error"
            return (
                Error(text=text).to_json(),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        text = "everything is up and running"
        return Message(text=text).to_json(), status.HTTP_200_OK

    # @health_check_namespace.doc("say_hello")
    # @inject
    # def get(
    #     self,
    #     service: HealthCheckService = Provide[AppContainer.service.healthcheck_service],
    # ):
    #     if not service.get_status():
    #         return (
    #             {"error": "the app is not ready to work as expected"},
    #             status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         )
    #
    #     return {"message": "everything is up and running"}, status.HTTP_200_OK
