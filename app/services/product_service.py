from app.models.umkm_models import db, Category, Product

class ProductService:
    def __init__(self, repo):
        self.repo = repo

    def get_products(self, page, per_page, search):
        return self.repo.get_all(page, per_page, search)

    def delete_product(self, product_id):
        return self.repo.delete(product_id)

    # Transaksi Atomik Multi-Tabel (Materi Pertemuan 7)
    def add_product_with_category(self, data):
        # Validasi Logika Bisnis (Syarat Pertemuan 4)
        if data.get("price") <= 0:
            return {"status": "fail", "errors": {"price": "Harga harus lebih besar dari 0"}}, 400

        try:
            # 1. Cek Kategori
            cat = Category.query.filter_by(name=data["category_name"]).first()
            if not cat:
                cat = Category(name=data["category_name"])
                db.session.add(cat)
                db.session.flush() # Ambil ID sementara sebelum commit permanen

            # 2. Buat Produk
            prod = Product(
                name=data["name"], 
                price=float(data["price"]), 
                stock=data.get("stock", 0), 
                category_id=cat.id,
                umkm_id=1 # Default UMKM Dummy
            )
            db.session.add(prod)
            db.session.commit() # Simpan permanen Kategori dan Produk
            
            return {"status": "success", "message": "Transaksi berhasil disimpan", "data": prod.to_dict()}, 201
            
        except Exception as e:
            db.session.rollback()
            return {"status": "error", "message": f"Transaksi dibatalkan (Rollback): {str(e)}"}, 500