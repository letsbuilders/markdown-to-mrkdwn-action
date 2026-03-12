FROM python:3.14-slim-trixie

RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

WORKDIR /converter

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=nonroot:nonroot src src

USER nonroot

CMD ["python3", "/converter/src/main.py"]