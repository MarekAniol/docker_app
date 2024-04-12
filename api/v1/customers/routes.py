from flask import Blueprint, jsonify, request
from common.services.customer_service import add_customer, delete_customer


customers_bp = Blueprint("customers",  __name__)


@customers_bp.route("/", methods=["GET"])
def get_customers():
    return jsonify({"message": "Customers loaded successful"})

@customers_bp.route("/", methods=["POST"])
def add_new_customer():
    customer_data = request.json
    return add_customer(customer_data)

@customers_bp.route("/<string:customer_id>", methods=["DELETE"])
def delete_customer_by_id(customer_id):
    return delete_customer(customer_id)