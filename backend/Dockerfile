FROM python:3.7.6
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN  pip install --upgrade pip
RUN pip install --default-timeout=100000 -r requirements.txt
# COPY ./static /code/static

EXPOSE 8000

