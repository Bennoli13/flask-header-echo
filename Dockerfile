# Use the official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application
COPY app.py .

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
