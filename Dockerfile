FROM pypy:3-7.3.0-slim

RUN useradd base_user

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# upgrade pip and install requirements
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

USER base_user

EXPOSE 8080

ENTRYPOINT ["gunicorn"]

CMD ["wsgi:app"]