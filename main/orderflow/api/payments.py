from flask import Blueprint, request, jsonify
from orderflow.services.payment_service import pay

bp = Blueprint("payments", __name__, url_prefix="/api/payments")

@bp.post("/charge")
def charge_order():
    order = request.get_json(force=True)
    return jsonify(pay(order))
