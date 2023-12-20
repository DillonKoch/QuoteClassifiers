# Use an official Ubuntu as a base image
FROM ubuntu:latest

# Set working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl git

# Install Python packages
RUN pip3 install torch torchvision torchaudio \
    numpy pandas matplotlib scikit-learn nltk tqdm \
    transformers autopep8

# Create a symbolic link to associate python with python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Copy the current directory contents into the container at /app
COPY . /app
