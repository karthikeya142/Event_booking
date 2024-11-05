 
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Database credentials
ENV DB_NAME=db.sqlite3      
ENV DB_USER=Event
ENV DB_PASSWORD=Event123
ENV DB_HOST=db             
ENV DB_PORT=5432        

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Collect static files (if applicable)
RUN python manage.py collectstatic --noinput

# Run migrations to create database tables
RUN python manage.py makemigrations


# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Event_book.wsgi:application"]
