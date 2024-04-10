from flask import Flask, jsonify, request
from common.services.customer_service import add_customer
from common.models.db_models import Categorie, db
from common.errors.custom_error_handlers import register_custom_errors_hadlers
from common.errors.http_error_handlers import register_http_error_handlers
from dotenv import load_dotenv
from os import getenv
load_dotenv()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =  getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)
register_custom_errors_hadlers(app)
register_http_error_handlers(app)


@app.route('/')
def hello_world():
    first_row = Categorie.query.first()
    if first_row is not None:
        return jsonify([{"Hello": first_row.category_name}])
    else:
        return 'Hello, no categories found!'

@app.route('/customer', methods=["POST"])
def add_new_customer():
    customer_data = request.json
    return add_customer(customer_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
