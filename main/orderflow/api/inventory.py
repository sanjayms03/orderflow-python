from flask import Blueprint, request, jsonify
from orderflow.services.inventory_service import reserve, restock

bp = Blueprint("inventory", __name__, url_prefix="/api/inventory")

@bp.post("/reserve")
def reserve_stock():
    body = request.get_json(force=True)
    return jsonify(reserve(body["product_id"], body["quantity"]))

@bp.post("/restock")
def restock_stock():
    body = request.get_json(force=True)
    return jsonify(restock(body["product_id"], body["quantity"]))
