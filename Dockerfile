FROM python:3.8

WORKDIR /srv 

RUN pip install --upgrade pip
RUN pip install -U selenium
RUN pip install mailjet_rest

RUN apt-get update && apt-get -y install cron
COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log