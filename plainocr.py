from PIL import Image
import pytesseract

# Optional: specify tesseract path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\zeeshan.ali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = 'image.png'  # Replace with your image file name
image = Image.open(image_path)

# Extract text
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
