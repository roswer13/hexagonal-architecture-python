import logging

from http import HTTPStatus

from rest_framework.views import exception_handler

from myapp.application.adapter.api.http import problem_response
from myapp.application.adapter.spi.persistence.exceptions.voting_user_not_found import (
    VotingUserNotFound
)


logger = logging.getLogger(__name__)


def exceptions_handler(exc, context):
    logger.error("Unexpected error occurred: %s", exc)

    response = exception_handler(exc, context)
    if response is not None:
        return response

    if isinstance(exc, VotingUserNotFound):
        return problem_response("Error", str(exc), HTTPStatus.NOT_FOUND)

    logger.exception("Unhandled error: %s", exc, exc_info=True)
    return problem_response(
        "Unknown error",
        "Our deepest apologies, an unexpected error occurred "
        "and we are already working on it.",
        HTTPStatus.INTERNAL_SERVER_ERROR
    )
