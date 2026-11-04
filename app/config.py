import os

class Config:
    # Menyimpan alamat koneksi ke MySQL menggunakan PyMySQL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:Yu$ufbwi123@localhost/katalog_pertanian_db'
    )
    
    # Menonaktifkan fitur pelacakan sinyal perubahan objek untuk menghemat memori server
    SQLALCHEMY_TRACK_MODIFICATIONS = False