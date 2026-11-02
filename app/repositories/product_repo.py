from app.models.umkm_models import db, Product

class ProductRepository:
    def get_all(self):
        return Product.query.all()

    def create(self, data):
        try:
            new_product = Product(
                name=data['name'],
                price=data['price'],
                stock=data.get('stock', 0),
                category_id=data['category_id'],
                umkm_id=data['umkm_id'] # Menggunakan ID UMKM
            )
            db.session.add(new_product)
            db.session.commit() # Transaksi Atomik
            return new_product
        except Exception as e:
            db.session.rollback() # Syarat mutlak UTS (Rollback jika gagal)
            print(f"Error Database: {e}")
            return None

    def update(self, product_id, data):
        try:
            product = Product.query.get(product_id)
            if not product:
                return None  # Mengembalikan None jika produk tidak ditemukan

            # Perbarui data jika field-nya dikirimkan dalam request
            if 'name' in data:
                product.name = data['name']
            if 'price' in data:
                product.price = data['price']
            if 'stock' in data:
                product.stock = data['stock']
            if 'category_id' in data:
                product.category_id = data['category_id']
            if 'umkm_id' in data:
                product.umkm_id = data['umkm_id']

            db.session.commit() # Transaksi Atomik
            return product
        except Exception as e:
            db.session.rollback() # Rollback jika terjadi kegagalan
            print(f"Error Database Update: {e}")
            return False # Mengembalikan False jika terjadi error sistem

    def delete(self, product_id):
        try:
            product = Product.query.get(product_id)
            if product:
                db.session.delete(product)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False