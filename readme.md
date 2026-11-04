# Sistem Katalog Produk UMKM Pertanian (Backend API)

Proyek ini dikembangkan untuk memenuhi tugas **Ujian Tengah Semester (UTS) Dasar Pemrograman Backend** di STIKOM PGRI Banyuwangi. Aplikasi ini merupakan RESTful API yang mengelola data produk-produk pertanian UMKM.

## 🛠️ Teknologi yang Digunakan
- **Framework:** Python Flask
- **Database:** MySQL
- **ORM:** Flask-SQLAlchemy
- **Arsitektur:** Layered Architecture (Model, Repository, Service, Route)

## 📂 Struktur Folder (Layered Architecture)
<<<<<<< HEAD
```text
=======
```
>>>>>>> ab2a4beaed3f94e753715c8f37197532c91d643c
katalog-umkm-pertanian/
│
├── app/
│   ├── models/           # Skema tabel database & Relasi (1:N)
│   ├── repositories/     # Logika CRUD, Paginasi & Search
│   ├── services/         # Logika Bisnis & Transaksi Atomik (Rollback)
│   ├── routes/           # Endpoint RESTful API (Controller)
│   ├── utils/            # Helper format response JSON (JSend)
│   ├── config.py         # Konfigurasi database
│   └── __init__.py       # Application Factory
│
├── katalog_pertanian.sql # File ekspor/dump database MySQL
├── seed.py               # Skrip untuk memasukkan data dummy
├── run.py                # File utama server
└── README.md             # Dokumentasi proyek
```

## 🚀 Daftar Endpoint API (v1)
Seluruh respons dibungkus menggunakan format Response Envelope yang terstandarisasi.

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| **GET** | `/api/v1/products` | Mengambil seluruh data katalog (Mendukung `page`, `per_page`, `search`) |
| **POST** | `/api/v1/products/transaction-demo` | Menambah data kategori & produk sekaligus (Transaksi Atomik / Rollback) |
| **DELETE**| `/api/v1/products/<id>` | Menghapus data produk berdasarkan ID |

## ⚙️ Cara Menjalankan Aplikasi Lokal
1. Pastikan Python dan MySQL (XAMPP/DBeaver) sudah terpasang dan berjalan.
2. Buat database kosong bernama `katalog_pertanian_db` di MySQL.
3. Buka terminal di folder proyek ini dan instal pustaka yang dibutuhkan:
    ```bash
    pip install Flask Flask-SQLAlchemy pymysql
    ```
4. Jalankan skrip seeder untuk membuat tabel dan mengisi 7 data awal:
    ```bash
    python seed.py
    ```
5. Jalankan server Flask:
<<<<<<< HEAD
    ```bash
    python run.py
    ```
6. API dapat diakses di `http://127.0.0.1:5000` menggunakan Postman.
=======
   python run.py
6. API dapat diakses di `http://127.0.0.1:5000` menggunakan Postman.
>>>>>>> ab2a4beaed3f94e753715c8f37197532c91d643c
