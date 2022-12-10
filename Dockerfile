FROM ubuntu:20.04 AS BASE
ENV TZ Europe/London
WORKDIR /opt/report_summarizer/API/

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt install apache2 python3 python3-pip python3-venv libapache2-mod-wsgi-py3 -y

COPY ./requirements.txt /opt/report_summarizer/API/requirements.txt

# Set up a python virtual environment for use and set it to the default
ENV VIRTUAL_ENV /opt/report_summarizer/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Install dependencies, gather all static files and check system 
RUN pip3 install -r requirements.txt

COPY ./src/analyst_report_summarizer /opt/report_summarizer/API/
RUN python3 /opt/report_summarizer/API/manage.py check
RUN python3 /opt/report_summarizer/API/manage.py collectstatic --noinput

# Copy apache config + keys into place
COPY ./build/apache_config_files/ /etc/apache2/sites-available/

# Ensure that the db.sqlite3 file exists and www-data can write to it
RUN touch /opt/report_summarizer/API/db.sqlite3 && \
	chmod 770 /opt/report_summarizer/API/db.sqlite3

# Configure permissions and enable site
RUN chown -R www-data:www-data /opt/report_summarizer/API && \
	chmod +x /opt/report_summarizer/API/analyst_report_summarizer/wsgi.py && \
	a2dissite 000-default && \
	a2ensite API

# Expose HTTP and HTTPS
EXPOSE 80/tcp
EXPOSE 443/tcp

# Docker containers only run whilst main process is ongoing, so apache must run in the foreground
CMD apachectl -D FOREGROUND