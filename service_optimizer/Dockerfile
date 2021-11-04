
FROM 3-slim-bullseye

ADD app.py /app.py
ADD requirements.txt /requirements.txt
ADD consumer.py /consumer.py

RUN pip install -r /requirements.txt
CMD ["python", "consumer.py"]
