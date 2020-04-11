FROM pypy:3-7.3.0-slim

# add a not privileged user
RUN useradd base_user

# create the application folder and set it as the working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# upgrade pip and install requirements
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# copy the application to the wd
COPY . /usr/src/app

# switch to not privileged user
USER base_user

EXPOSE 8080

ENTRYPOINT ["gunicorn"]

CMD ["wsgi:app"]