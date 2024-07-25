# Use the official Python image from the Docker Hub
FROM python:3.11.4-slim

# Set the working directory
WORKDIR /InmobiusApiAutomation

# Copy the requirements file to the container
COPY requirements.txt .

# Create a virtual environment
RUN python -m venv venv

# Install any needed packages specified in requirements.txt
# Use the virtual environment's pip to install the packages
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the environment variable to use the virtual environment
ENV PATH="/InmobiusApiAutomation/venv/bin:$PATH"

# Run the application or command as needed
# Example:
# CMD ["python", "app.py"]

# Optional: expose a port if your application runs a server
# EXPOSE 8000

