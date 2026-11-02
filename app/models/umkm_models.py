from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Relasi 1:N (Satu kategori punya banyak produk)
    products = db.relationship('Product', backref='category', lazy=True)

class Umkm(db.Model):
    __tablename__ = 'umkms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    # Relasi 1:N (Satu UMKM punya banyak produk)
    products = db.relationship('Product', backref='umkm', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, default=0)
    
    # Foreign Keys untuk menghubungkan ke tabel lain
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    umkm_id = db.Column(db.Integer, db.ForeignKey('umkms.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "category_id": self.category_id,
            "umkm_id": self.umkm_id
        }