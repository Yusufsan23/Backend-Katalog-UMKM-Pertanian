from flask import Blueprint, request
from app.repositories.product_repo import ProductRepository
from app.utils.response_helper import success_response, fail_response

product_bp_v1 = Blueprint("product_v1", __name__, url_prefix="/api/v1/products")
repo = ProductRepository()

@product_bp_v1.route("", methods=["GET"])
def get_products():
    products = repo.get_all()
    # Menggunakan to_dict() dari model untuk konversi ke JSON
    data = [p.to_dict() for p in products] 
    return success_response(data={"products": data, "total": len(data)})

@product_bp_v1.route("", methods=["POST"])
def add_product():
    body = request.get_json(silent=True)
    if not body:
        return fail_response({"body": "Data JSON tidak valid atau kosong"}, 400)

    # Validasi input sederhana
    if "name" not in body or "price" not in body or "category_id" not in body or "umkm_id" not in body:
        return fail_response({"error": "name, price, category_id, dan umkm_id wajib diisi"}, 400)

    # Memanggil fungsi create di repository (yang memiliki fitur atomic & rollback)
    new_product = repo.create(body)
    
    if new_product:
        return success_response(data=new_product.to_dict(), message="Produk berhasil ditambahkan", code=201)
    else:
        return fail_response({"server": "Gagal menyimpan data ke database (Rollback)"}, 500)
    
@product_bp_v1.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    body = request.get_json(silent=True)
    if not body:
        return fail_response({"body": "Data JSON tidak valid atau kosong"}, 400)

    # Memanggil fungsi update dari repository
    updated_product = repo.update(product_id, body)
    
    if updated_product is None:
        return fail_response({"id": "Produk tidak ditemukan"}, 404)
    elif updated_product is False:
        return fail_response({"server": "Gagal memperbarui data ke database (Rollback)"}, 500)
    
    return success_response(data=updated_product.to_dict(), message="Produk berhasil diperbarui")

@product_bp_v1.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    success = repo.delete(product_id)
    if success:
        return success_response(message="Produk berhasil dihapus")
    else:
        return fail_response({"id": "Produk tidak ditemukan atau gagal dihapus"}, 404)