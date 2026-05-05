from flask import Flask, jsonify, request
from app.model_handler import ModelHandler

app = Flask(__name__)

model_handler = ModelHandler('models/model.pkl')


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'JSON body is required'}), 400

        result = model_handler.predict(data)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)