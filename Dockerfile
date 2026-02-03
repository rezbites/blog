# Use Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements first (best practice)
COPY requirements.txt .

# Install libraries
RUN pip install -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "run.py"]
