from flask import jsonify

def success_response(data=None, message="Success", code=200):
    """
    Fungsi untuk membungkus respons sukses (2xx)
    """
    response = {
        "status": "success",
        "message": message
    }
    if data is not None:
        response["data"] = data
        
    return jsonify(response), code

def fail_response(errors=None, code=400):
    """
    Fungsi untuk membungkus respons gagal karena input/klien (4xx)
    """
    response = {
        "status": "fail"
    }
    if errors is not None:
        response["errors"] = errors
        
    return jsonify(response), code

def error_response(message="Internal Server Error", code=500):
    """
    Fungsi untuk membungkus respons error karena sistem/server (5xx)
    """
    response = {
        "status": "error",
        "message": message
    }
    return jsonify(response), code