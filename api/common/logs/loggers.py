import logging
from functools import wraps
from sqlalchemy.exc import DBAPIError
from common.errors.custom_errors import ValidationError


db_logger = logging.getLogger("app.database")
db_logger.setLevel(logging.WARNING)
app_logger = logging.getLogger("app.general")
app_logger.setLevel(logging.INFO)


def log_validation_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValidationError, DBAPIError) as e:
            db_logger.error("Error occurred: %s", str(e))
            raise e
    return wrapper
