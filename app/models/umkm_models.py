from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    # Syarat Pertemuan 7: Wajib menggunakan db.relationship
    products = db.relationship('Product', backref='category', lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Umkm(db.Model):
    __tablename__ = 'umkms'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    
    # Syarat Pertemuan 7: Wajib menggunakan db.relationship
    products = db.relationship('Product', backref='umkm', lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "owner": self.owner}

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    umkm_id = db.Column(db.Integer, db.ForeignKey('umkms.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            # Syarat Pertemuan 7: Gunakan backref
            "category": self.category.name if self.category else None,
            "umkm": self.umkm.name if self.umkm else None
        }