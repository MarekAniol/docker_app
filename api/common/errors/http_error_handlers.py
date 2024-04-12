from flask import jsonify
from common.helpers.format_error_response import format_error_response


def register_http_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return format_error_response(error, 400)

    @app.errorhandler(401)
    def unauthorize(error):
        return format_error_response(error, 401)
    
    @app.errorhandler(403)
    def forbidden(error):
        return format_error_response(error, 403)   
     
    @app.errorhandler(404)
    def not_found(error):
        return format_error_response(error, 404)
    
    @app.errorhandler(409)
    def conflict(error):
        return format_error_response(error, 409)

    @app.errorhandler(500)
    def internal_error(error):
        return format_error_response(error, 500)
    
    @app.errorhandler(503)
    def  service_unavailable(error):
        return format_error_response(error, 503)
    