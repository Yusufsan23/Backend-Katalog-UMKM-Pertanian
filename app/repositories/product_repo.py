from app.models.umkm_models import db, Product

class ProductRepository:
    def get_all(self, page=1, per_page=5, search=""):
        query = Product.query
        
        # Fitur Search (Materi Pertemuan 7)
        if search:
            query = query.filter(Product.name.ilike(f"%{search}%"))
            
        # Fitur Paginasi (Materi Pertemuan 7)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination

    def get_by_id(self, product_id):
        return db.session.get(Product, product_id)

    def delete(self, product_id):
        try:
            product = self.get_by_id(product_id)
            if product:
                db.session.delete(product)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False
    
    def update(self, product_id, data):
        try:
            product = self.get_by_id(product_id)
            if not product:
                return False
            
            # Ubah atribut jika dikirim oleh klien
            product.name = data.get("name", product.name)
            product.price = data.get("price", product.price)
            product.stock = data.get("stock", product.stock)
            
            db.session.commit() # Simpan permanen perubahan
            return True
        except Exception as e:
            db.session.rollback() # Batalkan jika gagal
            return False