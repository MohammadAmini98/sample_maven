# Use an official Python runtime as the base image
FROM python:3.9

WORKDIR /app

COPY ./app/requirements.txt /app/

RUN pip3 install -r /app/requirements.txt

COPY ./app /app

# Expose the port your Flask app is running on (default is 5000)
EXPOSE 5000

# Set the environment variable for Flask

# Run the Flask application when the container launches
CMD ["flask", "run"]
