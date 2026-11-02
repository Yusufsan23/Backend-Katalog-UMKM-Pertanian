# Sistem Katalog Produk UMKM Pertanian (Backend API)

Proyek ini dikembangkan untuk memenuhi tugas **Ujian Tengah Semester (UTS) Dasar Pemrograman Backend** di STIKOM PGRI Banyuwangi. Aplikasi ini merupakan RESTful API yang mengelola data produk-produk pertanian UMKM.

## 🛠️ Teknologi yang Digunakan
* **Framework:** Python Flask
* **Database:** MySQL
* **ORM:** Flask-SQLAlchemy
* **Arsitektur:** Layered Architecture (Model, Repository, Route)

## 📂 Struktur Folder (Layered Architecture)
katalog-umkm-pertanian/
│
├── app/
│   ├── models/           # Skema tabel database
│   ├── repositories/     # Logika CRUD & Transaksi Atomik
│   ├── routes/           # Endpoint RESTful API
│   └── utils/            # Helper format response JSON
│
├── katalog_pertanian.sql # File ekspor/dump database MySQL
├── seed.py               # Skrip untuk memasukkan data dummy
├── run.py                # File utama server
└── README.md             # Dokumentasi proyek

## 🚀 Daftar Endpoint API (v1)
Seluruh respons dibungkus menggunakan format Response Envelope yang terstandarisasi.

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| **GET** | `/api/v1/products` | Mengambil seluruh data katalog produk |
| **POST** | `/api/v1/products` | Menambah data produk pertanian baru |
| **PUT** | `/api/v1/products/<id>` | Memperbarui data produk berdasarkan ID |
| **DELETE**| `/api/v1/products/<id>` | Menghapus data produk berdasarkan ID |

## ⚙️ Cara Menjalankan Aplikasi Lokal
1. Pastikan Python dan MySQL (XAMPP/DBeaver) sudah terpasang dan berjalan.
2. Buat database kosong bernama `katalog_pertanian_db` di MySQL.
3. Buka terminal di folder proyek ini dan instal pustaka yang dibutuhkan:
   pip install Flask Flask-SQLAlchemy pymysql
4. Jalankan skrip seeder untuk membuat tabel dan mengisi 7 data awal:
   python seed.py
5. Jalankan server Flask:
   python run.py
6. API dapat diakses di `http://127.0.0.1:5000` menggunakan Postman.