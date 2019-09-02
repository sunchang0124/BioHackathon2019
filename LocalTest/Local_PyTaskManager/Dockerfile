FROM python:3.6-slim-stretch

RUN apt-get update && apt-get install -y python-pip

COPY FileService.py FileService.py

RUN pip install flask numpy

CMD ["python", "FileService.py"]