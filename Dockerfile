# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Copy the requirements.txt and install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Command to run the Python script
CMD ["python", "main.py"]