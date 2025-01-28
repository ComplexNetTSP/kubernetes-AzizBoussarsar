# Use Alpine as the base image
#FROM alpine:3.14

# Install system dependencies and Python
#RUN apk add --no-cache python3 py3-pip
FROM python:latest

# Set the working directory
WORKDIR /app

# Copy the application code and requirements file
# COPY requirements.txt requirements.txt
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Set the Flask app environment variable
ENV FLASK_APP=app

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
