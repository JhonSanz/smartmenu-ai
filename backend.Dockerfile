FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

EXPOSE 8000

COPY init.sh /init.sh
RUN chmod +x /init.sh
CMD ["./init.sh"] 
