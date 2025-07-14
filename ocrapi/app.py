from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract
import os
import subprocess


try:
    which_out = subprocess.check_output(['which', 'tesseract']).decode()
    print("🟢 Found tesseract at:", which_out)
except Exception as e:
    print("🔴 Could not find tesseract:", str(e))



app = Flask(__name__)
CORS(app)

# Use the env variable set in Dockerfile
#pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD', 'tesseract')
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"



@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    try:
        image_file = request.files['image']
        image = Image.open(image_file.stream)
        text = pytesseract.image_to_string(image)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check-tesseract', methods=['GET'])
def check_tesseract():
    import subprocess
    try:
        path = subprocess.check_output(['which', 'tesseract']).decode().strip()
        version = subprocess.check_output([path, '--version']).decode().strip()
        return jsonify({'path': path, 'version': version})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Render binds to PORT env var (default 10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
