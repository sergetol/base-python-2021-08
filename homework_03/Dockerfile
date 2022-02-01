# docker build -f Dockerfile -t homework_03-app:latest ./
# docker run -ti --rm -p 8000:8000/tcp homework_03-app:latest

FROM python:3.9-slim

WORKDIR /app

COPY ./app/requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app ./

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000" ]
