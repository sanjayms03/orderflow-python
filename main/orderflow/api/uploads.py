from flask import Blueprint, request, jsonify
import os
bp = Blueprint("uploads", __name__, url_prefix="/api/uploads")
@bp.post("")
def upload():
    file = request.files["file"]
    destination = os.path.join("/tmp/orderflow-uploads", file.filename)
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    file.save(destination)
    return jsonify({"saved": destination})
