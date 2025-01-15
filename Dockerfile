# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to /app
COPY . /app

# Copy the pre-downloaded wheels to a dedicated folder
COPY dependencies /dependencies

# Install the dependencies from the pre-downloaded wheels
RUN pip install --no-cache-dir /dependencies/*

# Expose the port your app runs on (adjust if needed)
EXPOSE 5000

# Define the command to run your app
CMD ["python", "app.py"]
