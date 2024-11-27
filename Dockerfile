FROM python:3.12-slim

WORKDIR /app

COPY ./app /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
#RUN pip install --timeout=60 -r requirements.txt --index-url https://pypi.python.org/simple/



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
