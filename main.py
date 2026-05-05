from flask import Flask, jsonify, request
from app.model_handler import ModelHandler
from app.logger import log_event


app = Flask(__name__)

model_handler = ModelHandler('models/model.pkl')


@app.route("/health", methods=["GET"])
def health():
    log_event({
        "endpoint": "/health",
        "status": "ok"
    })

    return jsonify({
        "status": "ok"
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if data is None:
            log_event({
                "endpoint": "/predict",
                "status": "error",
                "error": "JSON body is required"
            })
            return jsonify({'error': 'JSON body is required'}), 400

        result = model_handler.predict(data)

        log_event({
            "endpoint": "/predict",
            "status": "success",
            "model_version": result["model_version"],
            "prediction": result["prediction"],
            "probability": result["probability"]
        })

        return jsonify(result)

    except Exception as e:
        log_event({
            "endpoint": "/predict",
            "status": "error",
            "error": str(e)
        })
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)