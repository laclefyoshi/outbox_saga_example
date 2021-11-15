
FROM python:3-slim-bullseye
ADD app.py /app.py
ADD consumer.py /consumer.py
ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
ENTRYPOINT ["python", "/consumer.py"]
