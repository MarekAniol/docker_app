from flask import jsonify
from static.messages import SUCCESSFUL_ADDED_MESSAGE


def db_commit_success(entity_type):
    return jsonify({"error": False, "message": SUCCESSFUL_ADDED_MESSAGE.format(entity_type)})
