FROM python:3.10.17-bookworm

COPY ./app /app
COPY requirements.txt /app
COPY .env /app

RUN pip3 install -r app/requirements.txt
EXPOSE 80

CMD ["python3", "app/main.py"]