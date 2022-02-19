FROM tiangolo/uwsgi-nginx:python3.9

ENV PYTHONBUFFERED=1

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV DJANGO_DEBUG=0

COPY prestart.sh uwsgi.ini ./app ./

RUN chmod +x prestart.sh \
    && cp prestart.sh prestart.sh.bak \
    && tr -d '\r' < prestart.sh.bak > prestart.sh \
    && rm prestart.sh.bak
