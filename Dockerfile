FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev python3-dev && apk add gdal-dev

WORKDIR /app

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]
