# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=7860 \
    DASH_DEBUG_MODE=0

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose the port your app will run on
EXPOSE 7860

# Command to run the Dash app with gunicorn
CMD ["gunicorn", "app:server", "--bind", "0.0.0.0:7860", "--workers", "1"]
