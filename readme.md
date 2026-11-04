# Sistem Katalog Produk UMKM Pertanian (Backend API)

Proyek ini dikembangkan untuk memenuhi tugas **Ujian Tengah Semester (UTS) Dasar Pemrograman Backend** di STIKOM PGRI Banyuwangi. Aplikasi ini merupakan RESTful API yang mengelola data produk, kategori, dan profil UMKM di sektor pertanian dengan menerapkan arsitektur modular (*Layered Architecture*), integrasi ORM SQLAlchemy, serta manajemen transaksi atomik (ACID).

---

## 🛠️ Teknologi yang Digunakan
* **Framework:** Python Flask
* **Database:** MySQL
* **ORM:** Flask-SQLAlchemy & PyMySQL
* **Arsitektur:** Layered Architecture (Models, Repositories, Services, Routes, Utils)

---

## 📂 Struktur Folder (Layered Architecture)
```text
katalog-umkm-pertanian/
│
├── app/
│   ├── models/           # Skema tabel database (Categories, Umkms, Products)
│   ├── repositories/     # Logika Akses Data & Database Query (.paginate, .ilike)
│   ├── routes/           # Endpoint RESTful API (Product, Category, UMKM)
│   ├── services/         # Logika Bisnis & Transaksi Atomik (Rollback ACID)
│   ├── utils/            # Helper format response JSON (JSend / Response Envelope)
│   ├── config.py         # Konfigurasi Database & Environment
│   └── __init__.py       # Application Factory & Registrasi Blueprint
│
├── katalog_pertanian.sql # File ekspor/dump database MySQL
├── seed.py               # Skrip untuk memasukkan data dummy awal
├── run.py                # File utama (Entry Point) server Flask
└── README.md             # Dokumentasi proyek
```

---

## 🚀 Daftar Endpoint API (v1)
Seluruh respons API dibungkus menggunakan format *Response Envelope* yang terstandarisasi (`status`, `message`, `data`/`errors`).

### 1. Produk (Products)
| Method | Endpoint URI & Parameter | Deskripsi |
| :--- | :--- | :--- |
| **GET** | `/api/v1/products` | Menampilkan seluruh data produk |
| **GET** | `/api/v1/products?page=1&per_page=5&search=...` | Mengambil data produk dengan Paginasi & Search |
| **GET** | `/api/v1/products/<id>` | Menampilkan detail produk berdasarkan ID |
| **POST** | `/api/v1/products/transaction-demo` | Menambah kategori & produk baru secara bersamaan (Transaksi Atomik / Rollback) |
| **PUT** | `/api/v1/products/<id>` | Memperbarui data produk berdasarkan ID |
| **DELETE**| `/api/v1/products/<id>` | Menghapus data produk berdasarkan ID |

### 2. Kategori (Categories)
| Method | Endpoint URI & Parameter | Deskripsi |
| :--- | :--- | :--- |
| **GET** | `/api/v1/categories` | Menampilkan seluruh data kategori produk |
| **GET** | `/api/v1/categories/<id>` | Menampilkan detail kategori berdasarkan ID |
| **POST** | `/api/v1/categories` | Menambah data kategori baru |
| **PUT** | `/api/v1/categories/<id>` | Memperbarui nama kategori berdasarkan ID |
| **DELETE**| `/api/v1/categories/<id>` | Menghapus kategori berdasarkan ID |

### 3. UMKM (UMKMs)
| Method | Endpoint URI & Parameter | Deskripsi |
| :--- | :--- | :--- |
| **GET** | `/api/v1/umkms` | Menampilkan seluruh data UMKM pertanian |
| **GET** | `/api/v1/umkms/<id>` | Menampilkan detail UMKM berdasarkan ID |
| **POST** | `/api/v1/umkms` | Menambah profil UMKM baru |
| **PUT** | `/api/v1/umkms/<id>` | Memperbarui data UMKM berdasarkan ID |
| **DELETE**| `/api/v1/umkms/<id>` | Menghapus data UMKM berdasarkan ID |

---

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