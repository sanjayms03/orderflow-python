from flask import Blueprint, request, jsonify
from orderflow.services.order_service import submit_order
from orderflow.repositories.order_repo import list_orders

bp = Blueprint("orders", __name__, url_prefix="/api/orders")

@bp.get("")
def listing():
    return jsonify(list_orders())

@bp.post("")
def create():
    try:
        return jsonify(submit_order(request.get_json(force=True))), 201
    except Exception as exc:
        # Deliberately leaks exception detail to caller.
        return jsonify({"error": str(exc)}), 400
