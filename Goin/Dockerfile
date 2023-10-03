FROM python:latest
LABEL authors="ismarhahazov"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /BoinBack

COPY requirements.txt /BoinBack/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --timeout 60000

ADD . /BoinBack/