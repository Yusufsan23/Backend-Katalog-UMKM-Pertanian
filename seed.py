from app import create_app
from app.models.umkm_models import db, Category, Umkm, Product

app = create_app()

with app.app_context():
    # 1. Tambah Data Kategori
    kategori_data = ["Pupuk", "Bibit / Benih", "Alat Tani", "Hasil Panen"]
    for nama in kategori_data:
        if not Category.query.filter_by(name=nama).first():
            db.session.add(Category(name=nama))
    
    # 2. Tambah Data UMKM Dummy
    if not Umkm.query.filter_by(name="Kelompok Tani Makmur").first():
        db.session.add(Umkm(name="Kelompok Tani Makmur", owner="Pak Budi"))

    db.session.commit() # Simpan kategori & umkm dulu untuk mendapatkan ID

    # Ambil ID yang baru dibuat
    kat_pupuk = Category.query.filter_by(name="Pupuk").first().id
    kat_bibit = Category.query.filter_by(name="Bibit / Benih").first().id
    kat_alat = Category.query.filter_by(name="Alat Tani").first().id
    kat_panen = Category.query.filter_by(name="Hasil Panen").first().id
    umkm_id = Umkm.query.first().id

    # 3. Tambah 7 Data Produk
    produk_awal = [
        {"name": "Bibit Jagung Manis Super", "price": 75000, "stock": 50, "category_id": kat_bibit},
        {"name": "Pupuk NPK Organik", "price": 120000, "stock": 100, "category_id": kat_pupuk},
        {"name": "Alat Penyemprot Hama", "price": 250000, "stock": 15, "category_id": kat_alat},
        {"name": "Pupuk Kompos Organik", "price": 50000, "stock": 200, "category_id": kat_pupuk},
        {"name": "Benih Padi Inpari 32", "price": 85000, "stock": 80, "category_id": kat_bibit},
        {"name": "Cangkul Baja Hitam", "price": 150000, "stock": 30, "category_id": kat_alat},
        {"name": "Beras Merah Organik 5Kg", "price": 90000, "stock": 25, "category_id": kat_panen}
    ]

    for p in produk_awal:
        if not Product.query.filter_by(name=p["name"]).first():
            db.session.add(Product(**p, umkm_id=umkm_id))

    db.session.commit()
    print("Berhasil! 7 Data produk, kategori, dan UMKM telah dimasukkan ke database.")