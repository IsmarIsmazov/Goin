FROM python:3.10
LABEL authors="ismarhahazov"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /GoinBack

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --timeout 60000

ADD . /GoinBack/