from flask import jsonify
from static.messages import error_messages, LOG_ERROR
import common.logs.loggers as log


def format_error_response(error, status_code=None):
    if status_code is None:
        status_code = 500

    message = error_messages.get(type(error).__name__, getattr(error, 'message', str(error)))

    log_message = LOG_ERROR.format(message, error.__class__.__name__,  getattr(error, 'errors', ''))
    if status_code >= 500:
        log.app_logger.error(log_message)
    else:
        log.db_logger.error(log_message)

    return jsonify({"error": True, "message": message}), status_code
