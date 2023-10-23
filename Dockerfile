# Use the official Python image from the Docker Hub
FROM python:3.11.0

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
