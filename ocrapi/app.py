from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract
import os
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Optional: specify the path to tesseract executable

pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD', 'tesseract')
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\zeeshan.ali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    image_file = request.files['image']
    image = Image.open(image_file.stream)

    try:
        text = pytesseract.image_to_string(image)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
