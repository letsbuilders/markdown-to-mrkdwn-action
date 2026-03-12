FROM python:3.14-slim-trixie

WORKDIR /converter

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD src src

CMD ["python3", "/converter/src/main.py"]