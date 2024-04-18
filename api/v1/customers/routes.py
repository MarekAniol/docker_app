from flask import Blueprint, request
from common.helpers.entity_types import HttpMethodType
from common.helpers.successful_handlers import db_commit_success
from common.services.customer_service import add_customer, delete_customer


customers_bp = Blueprint("customers",  __name__)


@customers_bp.route("/", methods=["GET"])
def get_customers():
    return db_commit_success(http_method_type=HttpMethodType.GET)

@customers_bp.route("/", methods=["POST"])
def add_new_customer():
    customer_data = request.json
    return add_customer(customer_data)

@customers_bp.route("/<string:customer_id>", methods=["DELETE"])
def delete_customer_by_id(customer_id):
    return delete_customer(customer_id)