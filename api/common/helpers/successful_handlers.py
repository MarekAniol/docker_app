from flask import jsonify
from common.helpers.entity_types import HttpMethodType
from static.messages import (
    SUCCESS_MESSAGE,
    SUCCESSFUL_ADDED_MESSAGE,
    SUCCESSFUL_GET_MESSAGE,
    SUCCESSFUL_DELETE_MESSAGE,
    SUCCESSFUL_UPDATE_MESSAGE,
)


def db_commit_success(http_method_type, entity_type=None):
    def success_get():
        return jsonify({"error": False, "message": SUCCESSFUL_GET_MESSAGE}), 200

    def success_post():
        return (
            jsonify(
                {
                    "error": False,
                    "message": SUCCESSFUL_ADDED_MESSAGE.format(entity_type),
                }
            ),
            201,
        )

    def success_delete():
        return (
            jsonify(
                {
                    "error": False,
                    "message": SUCCESSFUL_DELETE_MESSAGE.format(entity_type),
                }
            ),
            200,
        )

    def success_put():
        return (
            jsonify(
                {
                    "error": False,
                    "message": SUCCESSFUL_UPDATE_MESSAGE.format(entity_type),
                }
            ),
            200,
        )

    def default():
        return (
            jsonify({"error": False, "message": SUCCESS_MESSAGE.format(entity_type)}),
            200,
        )

    mathod_switcher = {
        HttpMethodType.GET: success_get,
        HttpMethodType.POST: success_post,
        HttpMethodType.DELETE: success_delete,
        HttpMethodType.PUT: success_put,
    }
    return mathod_switcher.get(http_method_type, default)()
