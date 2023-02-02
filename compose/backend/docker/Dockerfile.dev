# The image you are going to inherit your Dockerfile from
FROM python:3.10
# Necessary, so Docker doesn't buffer the output and that you can see the output
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir opt/app
# Copy the requirements.txt file adjacent to the Dockerfile
# to your Docker image
COPY ./requirements.txt opt/requirements.txt
COPY ./start-server.sh opt/start-server.sh
# Install the requirements.txt file in Docker image
RUN pip install -r opt/requirements.txt

STOPSIGNAL SIGTERM
CMD ["/opt/start-server.sh"]