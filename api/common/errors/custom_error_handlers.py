from common.errors.custom_errors import JsonDataError, ValidationError
from common.helpers.format_error_response import format_custom_error_response
from static.messages import UNABLE_TO_SAVE_ERROR, NO_JSON_DATA
from common.helpers.entity_types import EntityType
    
    
def register_custom_errors_hadlers(app):
    @app.errorhandler(ValidationError)
    def validation_error(error):
        return format_custom_error_response(error, error.status_code)
    
    @app.errorhandler(JsonDataError)
    def json_data_error(error):
        return format_custom_error_response(error, error.status_code)
    