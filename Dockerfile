FROM python:3.12.0b1-slim-buster

RUN adduser -D docker-user

WORKDIR /etc/opt/site/

COPY . .

RUN pip install poetry==1.5.0
RUN poetry install --with production

RUN chmod +x boot.sh
RUN chown -R docker-user:docker-user ./

USER docker-user

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]