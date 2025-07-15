from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os

# Optional: Tesseract path (adjust only if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\zeeshan.ali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)

    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
