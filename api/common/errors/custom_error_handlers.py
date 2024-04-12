from common.errors.custom_errors import JsonDataError, ValidationError
from common.helpers.format_error_response import format_error_response
    
    
def register_custom_errors_hadlers(app):
    @app.errorhandler(ValidationError)
    def validation_error(error):
        return format_error_response(error, error.status_code)
    
    @app.errorhandler(JsonDataError)
    def json_data_error(error):
        return format_error_response(error, error.status_code)
    