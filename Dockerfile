<<<<<<< HEAD
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -e .

EXPOSE 5000

ENV FLASK_APP=application.py

CMD ["python" , "application.py"]
=======
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -e .

EXPOSE 5000

ENV FLASK_APP=application.py

CMD ["python" , "application.py"]
>>>>>>> afaeb17a88fcf97e9a4ada587857d23cd6c3bbbd
