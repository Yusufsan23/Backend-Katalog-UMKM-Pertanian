# Sistem Katalog Produk UMKM Pertanian (Backend API)

Proyek ini dikembangkan untuk memenuhi tugas **Ujian Tengah Semester (UTS) Dasar Pemrograman Backend** di STIKOM PGRI Banyuwangi. Aplikasi ini merupakan RESTful API yang mengelola data produk-produk pertanian UMKM.

## 🛠️ Teknologi yang Digunakan
* **Framework:** Python Flask
* **Database:** MySQL
* **ORM:** Flask-SQLAlchemy
* **Arsitektur:** Layered Architecture (Model, Repository, Route)

## 📂 Struktur Folder (Layered Architecture)
```text
katalog-umkm-pertanian/
│
├── app/
│   ├── models/           # Skema tabel database (categories, umkms, products)
│   ├── repositories/     # Logika CRUD & Transaksi Atomik (Rollback)
│   ├── routes/           # Endpoint RESTful API
│   └── utils/            # Helper format response JSON (JSend)
│
├── katalog_pertanian.sql # File ekspor/dump database MySQL
├── seed.py               # Skrip untuk memasukkan data awal dummy
├── run.py                # File utama untuk menjalankan server
└── README.md             # Dokumentasi proyek
```