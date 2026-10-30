FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install matplotlib
CMD ["python", "relogio.py"]
