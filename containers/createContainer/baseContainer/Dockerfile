# FROM python:2-stretch
FROM python:3.6-slim-stretch

RUN apt-get update && apt-get install -y r-base r-base-dev python-pip

RUN mkdir /data

RUN mkdir /encryption

RUN mkdir /output

COPY run.py run.py

RUN pip install mock pynacl crypto pycrypto pandas seaborn matplotlib numpy recordlinkage

ADD PQcrypto/PQencryption/ /usr/local/lib/python3.6/site-packages/PQencryption/

CMD ["python", "run.py"]
