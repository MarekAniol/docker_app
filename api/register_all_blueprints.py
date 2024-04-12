from flask import Flask
from static.url_config import CUSTOMERS_PREFIX

def register_app_blueprints(app: Flask):
    from v1.customers.routes import customers_bp

    app.register_blueprint(customers_bp, url_prefix=CUSTOMERS_PREFIX)