from flask import Blueprint, request, jsonify
from app.models.umkm_models import Category
from app.repositories.product_repo import ProductRepository
from app.services.product_service import ProductService
from app.utils.response_helper import success_response, fail_response

product_bp_v1 = Blueprint("product_v1", __name__, url_prefix="/api/v1/products")
category_bp_v1 = Blueprint("category_v1", __name__, url_prefix="/api/v1/categories")


# Inisialisasi Arsitektur
repo = ProductRepository()
service = ProductService(repo)

# 1. READ dengan Paginasi dan Search Parameter (Pertemuan 3 & 7)
@product_bp_v1.route("", methods=["GET"])
def get_products():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)
    search = request.args.get("search", "", type=str)

    pagination = service.get_products(page=page, per_page=per_page, search=search)
    
    data = [p.to_dict() for p in pagination.items]
    return jsonify({
        "status": "success",
        "data": data,
        "pagination": {
            "current_page": pagination.page,
            "per_page": pagination.per_page,
            "total_pages": pagination.pages,
            "total_items": pagination.total
        }
    }), 200


# 2. CREATE dengan Transaksi Atomik (Pertemuan 7)
@product_bp_v1.route("/transaction-demo", methods=["POST"])
def create_product():
    data = request.get_json(silent=True)
    if not data or not data.get("category_name") or not data.get("name") or data.get("price") is None:
        return fail_response({"error": "category_name, name, dan price wajib diisi"}, 400)

    # Kirim ke Service Layer untuk dicek aturan bisnisnya
    resp, code = service.add_product_with_category(data)
    return jsonify(resp), code

@product_bp_v1.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    # Logika penanganan update data
    data = request.get_json(silent=True)
    if not data:
        return fail_response({"error": "Data tidak valid"}, 400)

    resp, code = service.update_product(product_id, data)
    return jsonify(resp), code

# 3. DELETE (Pertemuan 3)
@product_bp_v1.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    success = service.delete_product(product_id)
    if success:
        return success_response(message="Produk berhasil dihapus")
    else:
        return fail_response({"id": "Produk tidak ditemukan atau gagal dihapus"}, 404)