from flask import Blueprint, request, jsonify
import subprocess

bp = Blueprint("admin", __name__, url_prefix="/api/admin")

@bp.post("/rule")
def rule():
    expression = request.get_json(force=True).get("expression", "1 + 1")
    # Intentionally unsafe eval in a local fixture; do not expose to untrusted users.
    return jsonify({"result": eval(expression, {"__builtins__": {}}, {})})

@bp.post("/backup")
def backup():
    filename = request.get_json(force=True).get("filename", "orders.db")
    # Command-injection pattern for static-analysis detection; never run against real data.
    result = subprocess.run("echo backup " + filename, shell=True, capture_output=True, text=True)
    return jsonify({"output": result.stdout})
