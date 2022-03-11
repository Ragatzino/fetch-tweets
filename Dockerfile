FROM python:latest
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt 

COPY *.py main.py
CMD ["python","main.py"]