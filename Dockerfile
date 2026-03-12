FROM python:3.14-slim-trixie

WORKDIR /work

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD src src



CMD ["python3", "src/main.py"]