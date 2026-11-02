from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Yu$ufbwi123@localhost/katalog_pertanian_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Mendaftarkan model dan membuat tabel otomatis di database
    with app.app_context():
        from app.models import umkm_models
        db.create_all()
        
        from app.routes.product_routes import product_bp_v1
        app.register_blueprint(product_bp_v1)
        
    return app