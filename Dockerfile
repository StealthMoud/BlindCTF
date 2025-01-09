# Use Python slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the default command to run the Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
