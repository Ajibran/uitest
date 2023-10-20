FROM python:3.8

WORKDIR /srv 

RUN pip install --upgrade pip
RUN pip install -U selenium
RUN pip install mailjet_rest