from flask import Flask
from app.config import Config
from app.models.umkm_models import db
from app.routes.product_routes import product_bp_v1
from app.routes.categories_routes import category_bp_v1
from app.routes.umkm_routes import umkm_bp_v1
from app.utils.response_helper import fail_response

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi Database
    db.init_app(app)

    # Buat tabel otomatis jika belum ada (Bisa dihapus jika mengandalkan seeder)
    with app.app_context():
        db.create_all()

    # Mendaftarkan Blueprint Route
    app.register_blueprint(product_bp_v1)
    app.register_blueprint(category_bp_v1)
    app.register_blueprint(umkm_bp_v1)

    # Global Error Handlers (Opsional namun disarankan)
    @app.errorhandler(404)
    def page_not_found(error):
        return fail_response({"url": "Endpoint API tidak ditemukan."}, 404)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return fail_response({"method": "Metode HTTP tidak diizinkan."}, 405)

    @app.errorhandler(500)
    def internal_server_error(error):
        return fail_response({"server": "Terjadi kesalahan internal."}, 500)

    return app