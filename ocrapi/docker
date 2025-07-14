FROM python:3.10-slim

# Install system packages and Tesseract
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN which tesseract && tesseract --version  # <-- Add this line


# Set working directory
WORKDIR /app

# Copy dependency file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Set Tesseract path for pytesseract
ENV TESSERACT_CMD=/usr/bin/tesseract

# Tell Flask to listen on 0.0.0.0, port 10000 (Render uses this)
ENV PORT=10000

# Expose the correct port
EXPOSE 10000

# Start the app
CMD ["python", "app.py"]
