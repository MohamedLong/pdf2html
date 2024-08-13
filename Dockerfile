# Use Ubuntu Bionic base image
FROM ubuntu:bionic

# Install system dependencies and Python 3 with pip
RUN apt-get update && \
    apt-get install -y \
    wget \
    fontforge \
    libpoppler-cpp-dev \
    libcairo2-dev \
    libpango1.0-dev \
    git \
    build-essential \
    fonts-freefont-ttf \
    libjpeg-turbo8 \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create /tmp directory with correct permissions
RUN mkdir -p /tmp && chmod 1777 /tmp

# Copy the .deb package into the container
COPY pdf2htmlEX.deb /pdf2htmlEX.deb

# Install the .deb package and fix dependencies
RUN dpkg -i /pdf2htmlEX.deb && \
    apt-get -f install -y && \
    rm /pdf2htmlEX.deb

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]
