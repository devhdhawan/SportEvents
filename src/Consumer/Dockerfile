# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port Flask runs on
EXPOSE 5000

# Entry point to run your consumer Flask app
CMD ["python", "Consumer.py"]
