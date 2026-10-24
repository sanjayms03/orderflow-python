from flask import Blueprint, request, jsonify
from orderflow.repositories.customer_repo import find_customer, create_customer

bp = Blueprint("customers", __name__, url_prefix="/api/customers")

@bp.get("")
def search():
    name = request.args.get("name", "")
    return jsonify(find_customer(name))

@bp.post("")
def create():
    data = request.get_json(force=True)
    return jsonify(create_customer(data.get("name", ""), data.get("email", ""))), 201
