# Sistem Katalog Produk UMKM Pertanian (Backend API)

Proyek ini dikembangkan untuk memenuhi tugas **Ujian Tengah Semester (UTS) Dasar Pemrograman Backend** di STIKOM PGRI Banyuwangi. Aplikasi ini merupakan RESTful API yang mengelola data produk-produk pertanian UMKM dengan menerapkan arsitektur modular, *Layered Architecture*, integrasi ORM SQLAlchemy, serta manajemen transaksi atomik (ACID).

## 🛠️ Teknologi yang Digunakan
* **Framework:** Python Flask
* **Database:** MySQL
* **ORM:** Flask-SQLAlchemy & PyMySQL
* **Arsitektur:** Layered Architecture (Models, Repositories, Services, Routes, Utils)

## 📂 Struktur Folder (Layered Architecture)
```text
katalog-umkm-pertanian/
│
├── app/
│   ├── __init__.py       # Application Factory & Registrasi Blueprint
│   ├── config.py         # Konfigurasi Database & Environment
│   ├── models/           # Skema tabel database (Categories, Umkms, Products)
│   ├── repositories/     # Logika Akses Data & Database Query (.paginate, .ilike)
│   ├── routes/           # Endpoint Controller RESTful API
│   ├── services/         # Logika Bisnis & Transaksi Atomik (Rollback ACID)
│   └── utils/            # Helper format response JSON (JSend)
│
├── katalog_pertanian.sql # File ekspor/dump database MySQL
├── seed.py               # Skrip untuk memasukkan data dummy awal
├── run.py                # File utama (Entry Point) server Flask
└── README.md             # Dokumentasi proyek
```

## 🚀 Daftar Endpoint API (v1)
Seluruh respons API dibungkus menggunakan format *Response Envelope* yang terstandarisasi.

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| **GET** | `/api/v1/products` | Mengambil seluruh data produk dengan fitur Paginasi (`?page=1&per_page=5`) & Search (`?search=...`) |
| **POST** | `/api/v1/products/transaction-demo` | Menambah kategori dan produk baru secara bersamaan melalui Transaksi Atomik (Multi-Tabel) |
| **PUT** | `/api/v1/products/<id>` | Memperbarui data produk berdasarkan ID |
| **DELETE**| `/api/v1/products/<id>` | Menghapus data produk berdasarkan ID |

## ⚙️ Cara Menjalankan Aplikasi Lokal
1. Pastikan Python dan MySQL (XAMPP/DBeaver) sudah terpasang dan berjalan.
2. Buat database kosong bernama `katalog_pertanian_db` di MySQL.
3. Buka terminal di folder proyek ini dan instal pustaka yang dibutuhkan:
   ```bash
   pip install Flask Flask-SQLAlchemy pymysql
   ```
4. Jalankan skrip *seeder* untuk membuat tabel dan mengisi data awal secara otomatis:
   ```bash
   python seed.py
   ```
5. Jalankan server Flask:
   ```bash
   python run.py
   ```
6. API siap diuji melalui Postman di alamat `http://127.0.0.1:5000`.