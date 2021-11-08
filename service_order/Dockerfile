
FROM python:3-slim-bullseye
ADD app.py /app.py
ADD producer.py /producer.py
ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
CMD ["python", "/producer.py"]
