from flask import Flask, request, jsonify
from flask_cors import CORS
import os

PORT = int(os.environ.get("PORT", 7000))



app = Flask(__name__)

CORS(app)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/api", methods=["POST"])
def api():
    data = request.json

    return jsonify({
        "message": "Data received successfully",
        "data": data
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)