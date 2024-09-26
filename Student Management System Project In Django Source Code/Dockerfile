# Use the official Python image as a base
FROM python:3

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install django==4.2.5 mysqlclient

# Copy the project files into the container
COPY . .

# Run database migrations
RUN python manage.py migrate

# Expose the port your application will run on
EXPOSE 8001

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

