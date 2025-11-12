FROM python:3.11-slim

RUN apt-get update && apt-get install -y systemd procps && apt-get clean

WORKDIR /app
COPY app.py /app/app.py
RUN pip install flask

EXPOSE 8080
CMD ["python", "app.py"]
