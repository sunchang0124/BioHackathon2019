FROM python:3.6-slim-stretch

RUN apt-get update && apt-get install -y python-pip

COPY SplitDatasets.py SplitDatasets.py

COPY input.json input.json

COPY Generated_Datasets Generated_Datasets

RUN pip install pandas numpy

CMD ["python", "SplitDatasets.py"]