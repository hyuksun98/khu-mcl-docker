# Use the official Python base image
FROM python:3.8

# Define a build-time variable and set environment variable
ARG USER_NAME
ENV USER=${USER_NAME}

# Set environment variable for the app's home directory
ENV APP_HOME=/app

# Set environment variable for the Flask server port
ENV FLASK_PORT=5000

# Change the working directory to the app's home directory
WORKDIR $APP_HOME

# Copy the current directory contents into the container at the app's home directory
COPY . $APP_HOME

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Change the directory to the /Flask
WORKDIR $APP_HOME/Flask

# Expose port 5000 to the outside world (documentation purpose)
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]

