FROM python:3.8-alpine

RUN apk update
RUN apk --update add ucspi-tcp
RUN apk --update add alpine-sdk && apk add libffi-dev openssl-dev

WORKDIR /usr/src/app

COPY src/requirements.txt .
RUN pip install -qr requirements.txt
COPY src/ .

EXPOSE 5000

CMD ["python3", "server.py"]