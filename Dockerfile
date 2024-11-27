FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Set the start command
CMD ["bash", "start.sh"]
