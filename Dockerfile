FROM python:3.10-slim

WORKDIR /app

COPY app /app

RUN pip install PyPDF2

CMD ["python", "extract_outline.py"]
