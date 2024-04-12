from flask import Flask, jsonify, request
from common.errors.dbapi_error_handlers import register_DBAPIError_errors_hadlers
from common.services.customer_service import add_customer
from common.models.db_models import Categorie, db
from common.errors.custom_error_handlers import register_custom_errors_hadlers
from common.errors.http_error_handlers import register_http_error_handlers
from dotenv import load_dotenv
from os import getenv
from register_all_blueprints import register_app_blueprints
load_dotenv()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =  getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)

register_custom_errors_hadlers(app)
register_http_error_handlers(app)
register_app_blueprints(app)
register_DBAPIError_errors_hadlers(app)

@app.route('/')
def hello_world():
    return 'Hello, welcome to Flask application!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
