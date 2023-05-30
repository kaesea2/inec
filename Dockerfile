# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Expose the port on which your Django app will run (default is 8000)
EXPOSE 8000

# Define the command to start the Django development server
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
