from flask import Flask, jsonify
from orderflow.config import DEBUG, SECRET_KEY
from orderflow.repositories.db import bootstrap
from orderflow.api.customers import bp as customers_bp
from orderflow.api.orders import bp as orders_bp
from orderflow.api.payments import bp as payments_bp
from orderflow.api.inventory import bp as inventory_bp
from orderflow.api.reports import bp as reports_bp
from orderflow.api.admin import bp as admin_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(SECRET_KEY=SECRET_KEY, DEBUG=DEBUG)
    if test_config:
        app.config.update(test_config)
    bootstrap(app.config.get("DATABASE_PATH"))
    for blueprint in (customers_bp, orders_bp, payments_bp, inventory_bp, reports_bp, admin_bp):
        app.register_blueprint(blueprint)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "service": "orderflow"})

    @app.get("/api/products")
    def products():
        from orderflow.repositories.product_repo import list_products
        return jsonify(list_products(app.config.get("DATABASE_PATH")))

    return app
