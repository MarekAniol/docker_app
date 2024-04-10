from static.messages import NO_JSON_DATA, UNABLE_TO_SAVE_ERROR
from common.helpers.entity_types import EntityType


class CustomError(Exception):
    def __init__(self, message=None, status_code=None, errors= None):
        super().__init__(message, status_code, errors)
        self.message = message if message is not None else "An error occurred"
        self.status_code = status_code if status_code is not None else 500
        self.errors = errors

class ValidationError(CustomError):
    """Exception raised for errors due to a bad request from the client."""
    def __init__(self, entity_type=EntityType.RECORD, message=None, errors=None, status_code=400):
        if message is None:
            message = UNABLE_TO_SAVE_ERROR.format(entity_type)
        super().__init__(message, status_code)
        self.errors = errors
        self.message = message
        self.status_code = status_code

class JsonDataError(CustomError):
    """Exception rised when there is no JSON data in request."""
    def __init__(self, message=None, errors=None, status_code=400):
        message = NO_JSON_DATA
        super().__init__(message, status_code)
        self.errors = errors
        self.message = message
        self.status_code = status_code