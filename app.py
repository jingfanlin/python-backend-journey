# app.py
from flask import Flask, jsonify
from logic import get_status_info, InvalidStatusError, StatusNotFoundError

app = Flask(__name__)

# 400：参数不合法
@app.errorhandler(InvalidStatusError)
def handle_invalid_status(error):
    return jsonify({"ok": False, "error": f"invalid status: {error}"}), 400

# 404：资源不存在
@app.errorhandler(StatusNotFoundError)
def handle_status_not_found(error):
    return jsonify({"ok": False, "error": f"status not found: {error}"}), 404

@app.route("/status/<status>")
def status_api(status):
    info = get_status_info(status)
    return jsonify({"ok": True, "data": info}), 200

if __name__ == "__main__":
    app.run(debug=True)