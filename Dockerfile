FROM python:3.12-alpine

WORKDIR /app

COPY app/ /app/

RUN python -m py_compile app.py

EXPOSE 8080

CMD ["python", "-u", "app.py"]

