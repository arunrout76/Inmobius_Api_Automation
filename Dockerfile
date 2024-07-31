# # Use the official Python image from the Docker Hub
# FROM python:3.11.4-slim

# # Install required tools
# RUN apt-get update && apt-get install -y \
#     curl \
#     unzip \
#     openjdk-11-jre-headless

# # Install Allure Command-Line tools (version 2.13.2)
# RUN curl -o /tmp/allure.zip -L https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.2/allure-commandline-2.13.2.zip \
#     && unzip /tmp/allure.zip -d /opt/ \
#     && ln -s /opt/allure-2.13.2/bin/allure /usr/bin/allure

# # # Set environment paths for Python, Selenium, Java, and Allure binaries
# # ENV PATH $PATH:/usr/bin:/opt/allure-2.13.2/bin

# # # Set the environment variable to use the virtual environment
# # ENV PATH="/InmobiusApiAutomation/venv/bin:$PATH"

# # Set the working directory
# WORKDIR /InmobiusApiAutomation

# # Copy the requirements file to the container
# COPY requirements.txt .

# # Create a virtual environment
# RUN python -m venv venv

# # Install any needed packages specified in requirements.txt
# # Use the virtual environment's pip to install the packages
# RUN venv/bin/pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code to the container
# COPY . .

# # Set environment paths for Python, Selenium, Java, and Allure binaries
# ENV PATH="/InmobiusApiAutomation/venv/bin:/usr/bin:/opt/allure-2.13.2/bin:$PATH"

# # Run the application or command as needed
# # Example:
# # CMD ["python", "app.py"]

# # Optional: expose a port if your application runs a server
# # EXPOSE 8000

# Use the official Python image from the Docker Hub
FROM python:3.11.4-slim

# Install required tools and Java
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    openjdk-11-jdk \
    && rm -rf /var/lib/apt/lists/*

# Install Allure Command-Line tools (version 2.13.2)
RUN curl -o /tmp/allure.zip -L https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.2/allure-commandline-2.13.2.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && ln -s /opt/allure-2.13.2/bin/allure /usr/bin/allure \
    && rm /tmp/allure.zip


# Set environment variables for Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:/InmobiusApiAutomation/venv/bin:/usr/bin:/opt/allure-2.13.2/bin:$PATH"


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

# Run the application or command as needed
# Example:
# CMD ["python", "app.py"]

# Optional: expose a port if your application runs a server
# EXPOSE 8000
