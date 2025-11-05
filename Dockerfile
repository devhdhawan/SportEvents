# Use official Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files
COPY . .

# Expose port (e.g., Flask default 5000)
EXPOSE 5000

# Command to run your backend service
CMD ["python", "server.py"]
