# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Flask
RUN pip install flask

# Expose port 5001 to the outside
EXPOSE 5001

# Run the Flask application
CMD ["python3", "python_server.py"]
