from flask import Blueprint, request
from app.models.umkm_models import db, Category
from app.utils.response_helper import success_response, fail_response

category_bp_v1 = Blueprint("category_v1", __name__, url_prefix="/api/v1/categories")

# 1. READ ALL (GET - Menampilkan semua kategori)
@category_bp_v1.route("", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return success_response(data=[cat.to_dict() for cat in categories])

# 2. READ BY ID (GET - Menampilkan satu kategori berdasarkan ID)
@category_bp_v1.route("/<int:category_id>", methods=["GET"])
def get_category_by_id(category_id):
    category = Category.query.get(category_id)
    if not category:
        return fail_response({"id": "Kategori tidak ditemukan"}, 404)
    return success_response(data=category.to_dict(), message="Detail kategori berhasil diambil")

# 3. CREATE (POST - Menambah kategori baru)
@category_bp_v1.route("", methods=["POST"])
def create_category():
    data = request.get_json(silent=True)
    if not data or not data.get("name"):
        return fail_response({"error": "Nama kategori wajib diisi"}, 400)
    
    try:
        new_category = Category(name=data["name"])
        db.session.add(new_category)
        db.session.commit()
        return success_response(data=new_category.to_dict(), message="Kategori berhasil ditambahkan", code=201)
    except Exception as e:
        db.session.rollback()
        return fail_response({"error": str(e)}, 500)

# 4. UPDATE (PUT - Memperbarui kategori berdasarkan ID)
@category_bp_v1.route("/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    data = request.get_json(silent=True)
    if not data or not data.get("name"):
        return fail_response({"error": "Nama kategori baru wajib diisi"}, 400)
    
    try:
        category = Category.query.get(category_id)
        if not category:
            return fail_response({"id": "Kategori tidak ditemukan"}, 404)
        
        category.name = data["name"]
        db.session.commit()
        return success_response(data=category.to_dict(), message="Kategori berhasil diperbarui")
    except Exception as e:
        db.session.rollback()
        return fail_response({"error": str(e)}, 500)

# 5. DELETE (DELETE - Menghapus kategori berdasarkan ID)
@category_bp_v1.route("/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    try:
        category = Category.query.get(category_id)
        if not category:
            return fail_response({"id": "Kategori tidak ditemukan"}, 404)
        
        db.session.delete(category)
        db.session.commit()
        return success_response(message="Kategori berhasil dihapus")
    except Exception as e:
        db.session.rollback()
        return fail_response({"error": str(e)}, 500)