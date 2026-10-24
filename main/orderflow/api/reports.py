from flask import Blueprint, request, jsonify
from orderflow.services.report_service import render_report, export_name

bp = Blueprint("reports", __name__, url_prefix="/api/reports")

@bp.get("/preview")
def preview():
    title = request.args.get("title", "Order report")
    html = render_report(title, ["created", "paid", "shipped"])
    return html

@bp.get("/export")
def export():
    return jsonify({"path": export_name(request.args.get("name", "orders"))})
