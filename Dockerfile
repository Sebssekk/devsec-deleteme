FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py

RUN pip install -r requirements.txt

CMD ["python", "main.py"]