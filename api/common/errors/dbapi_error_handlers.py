from sqlalchemy.exc import (
    InterfaceError,
    DatabaseError,
    DataError,
    OperationalError,
    InternalError,
    ProgrammingError,
    IntegrityError,
    NotSupportedError,
)
from common.helpers.format_error_response import format_error_response


def register_dba_api_error_errors_hadlers(app):
    @app.errorhandler(InterfaceError)
    def interface_error(error):
        status_code = 503
        return format_error_response(error, status_code)

    @app.errorhandler(DatabaseError)
    def database_error(error):
        status_code = 500
        return format_error_response(error, status_code)

    @app.errorhandler(DataError)
    def data_error(error):
        status_code = 400
        return format_error_response(error, status_code)

    @app.errorhandler(OperationalError)
    def operational_error(error):
        status_code = 500
        return format_error_response(error, status_code)

    @app.errorhandler(InternalError)
    def integrity_error(error):
        status_code = 409
        return format_error_response(error, status_code)

    @app.errorhandler(ProgrammingError)
    def internal_error(error):
        status_code = 500
        return format_error_response(error, status_code)

    @app.errorhandler(IntegrityError)
    def programming_error(error):
        status_code = 400
        return format_error_response(error, status_code)

    @app.errorhandler(NotSupportedError)
    def not_supported_error(error):
        status_code = 501
        return format_error_response(error, status_code)
