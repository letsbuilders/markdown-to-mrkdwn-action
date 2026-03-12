FROM python:3.14-slim-trixie

RUN groupadd --system --gid 1001 nonroot \
 && useradd --system --gid 1001 --uid 1001 --create-home nonroot

WORKDIR /converter

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=nonroot:nonroot src src

USER nonroot

CMD ["python3", "/converter/src/main.py"]