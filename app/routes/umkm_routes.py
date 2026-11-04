from flask import Blueprint, request
from app.models.umkm_models import db, Umkm
from app.utils.response_helper import success_response, fail_response

umkm_bp_v1 = Blueprint("umkm_v1", __name__, url_prefix="/api/v1/umkms")

# 1. READ ALL (GET - Menampilkan semua data UMKM)
@umkm_bp_v1.route("", methods=["GET"])
def get_umkms():
    umkms = Umkm.query.all()
    return success_response(data=[u.to_dict() for u in umkms])

# 2. READ BY ID (GET - Menampilkan satu UMKM berdasarkan ID)
@umkm_bp_v1.route("/<int:umkm_id>", methods=["GET"])
def get_umkm_by_id(umkm_id):
    umkm = Umkm.query.get(umkm_id)
    if not umkm:
        return fail_response({"id": "UMKM tidak ditemukan"}, 404)
    return success_response(data=umkm.to_dict(), message="Detail UMKM berhasil diambil")

# 3. CREATE (POST - Menambah data UMKM baru)
@umkm_bp_v1.route("", methods=["POST"])
def create_umkm():
    data = request.get_json(silent=True)
    if not data or not data.get("name") or not data.get("owner"):
        return fail_response({"error": "Nama UMKM dan owner (pemilik) wajib diisi"}, 400)
    
    try:
        new_umkm = Umkm(
            name=data["name"],
            owner=data["owner"]
        )
        db.session.add(new_umkm)
        db.session.commit()
        return success_response(data=new_umkm.to_dict(), message="UMKM berhasil ditambahkan", code=201)
    except Exception as e:
        db.session.rollback()
        return fail_response({"error": str(e)}, 500)

# 4. UPDATE (PUT - Memperbarui data UMKM berdasarkan ID)
@umkm_bp_v1.route("/<int:umkm_id>", methods=["PUT"])
def update_umkm(umkm_id):
    data = request.get_json(silent=True)
    if not data:
        return fail_response({"error": "Data tidak valid"}, 400)
    
    try:
        umkm = Umkm.query.get(umkm_id)
        if not umkm:
            return fail_response({"id": "UMKM tidak ditemukan"}, 404)
        
        umkm.name = data.get("name", umkm.name)
        umkm.owner = data.get("owner", umkm.owner)
        
        db.session.commit()
        return success_response(data=umkm.to_dict(), message="UMKM berhasil diperbarui")
    except Exception as e:
        db.session.rollback()
        return fail_response({"error": str(e)}, 500)

# 5. DELETE (DELETE - Menghapus data UMKM berdasarkan ID)
@umkm_bp_v1.route("/<int:umkm_id>", methods=["DELETE"])
def delete_umkm(umkm_id):
    try:
        umkm = Umkm.query.get(umkm_id)
        if not umkm:
            return fail_response({"id": "UMKM tidak ditemukan"}, 404)
        
        db.session.delete(umkm)
        db.session.commit()
        return success_response(message="UMKM berhasil dihapus")
    except Exception as e:
        db.session.rollback()
        return fail_response({"error": str(e)}, 500)