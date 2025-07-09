from PIL import Image
import pytesseract

# Optional: specify tesseract path if not in environment variables
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\zeeshan.ali\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Load the image
image = Image.open('image.png')  # replace with your image file

# Extract text
text = pytesseract.image_to_string(image)

# Print the result
print("Extracted Text:\n", text)
