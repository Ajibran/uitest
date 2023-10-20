FROM python:3.8

WORKDIR .
COPY . .

EXPOSE 9222

RUN pip install --upgrade pip
RUN pip install -U selenium
RUN pip install mailjet_rest
RUN pip install webdriver-manager

#RUN apt-get update && apt-get -y install cron
#COPY cron /etc/cron.d/cron
#RUN chmod 0644 /etc/cron.d/cron
#RUN crontab /etc/cron.d/cron
#RUN touch /var/log/cron.log
#CMD cron && tail -f /var/log/cron.log



# Install chromedriver
#RUN wget -N https://chromedriver.storage.googleapis.com/72.0.3626.69/chromedriver_linux64.zip -P ~/
#RUN unzip ~/chromedriver_linux64.zip -d ~/
#RUN rm ~/chromedriver_linux64.zip
#RUN mv -f ~/chromedriver /usr/local/bin/chromedriver
#RUN chown root:root /usr/local/bin/chromedriver
#RUN chmod 0755 /usr/local/bin/chromedriver


# Install chrome broswer
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable
