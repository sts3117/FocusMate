from flask import Flask, request, jsonify
from flask_cors import CORS   # 추가!!
import os
import base64
from datetime import datetime

app = Flask(__name__)
CORS(app)  # CORS 허용

SAVE_FOLDER = 'saved_faces'
os.makedirs(SAVE_FOLDER, exist_ok=True)

@app.route('/save_face_image', methods=['POST'])
def save_face_image():
    try:
        data = request.get_json()
        image_data = data['image']

        header, encoded = image_data.split(",", 1)
        img_bytes = base64.b64decode(encoded)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"face_{timestamp}.jpg"
        filepath = os.path.join(SAVE_FOLDER, filename)

        with open(filepath, 'wb') as f:
            f.write(img_bytes)

        return jsonify({"message": "Face image saved.", "filename": filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analyze_pose', methods=['POST'])
def analyze_pose():
    try:
        data = request.get_json()
        image_data = data['image']

        # 실제 포즈 분석 대신 더미 데이터 리턴
        result = {
            "pose_status": "good",
            "details": "Standing straight"
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
