from static.messages import LOG_ERROR
import common.logs.loggers as log
from flask import jsonify

def format_custom_error_response(error, status_code):
    log_message = LOG_ERROR.format(error.__class__.__name__, error.message, error.errors)

    if status_code >= 500:
        log.app_logger.error(log_message)
    else: 
        log.db_logger.error(log_message)

    return jsonify({"error": True, "message": error.message}), status_code


def format_standard_error_response (error, status_code):
    log_message = LOG_ERROR.format(error.__class__.__name__, str(error))

    if status_code >= 500:
        log.app_logger.error(log_message) 
    else: 
        log.db_logger.error(log_message)

    return jsonify({"error": True, "message": str(error)}), status_code