FROM python:3.10-slim
ENV TOKEN='7718484010:AAF9UNcrSEa0ncRUFI_qPmwfYkFg-P0duMo'
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]