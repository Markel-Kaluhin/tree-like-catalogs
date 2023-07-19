FROM python:3.11.1

WORKDIR /src/be/

RUN apt update \
        && apt -y install nginx \
        && apt clean \
        && ln -sf /dev/stdout /var/log/nginx/access.log \
        && ln -sf /dev/stderr /var/log/nginx/error.log

COPY nginx.conf /etc/nginx/nginx.conf

RUN pip install --upgrade pip && pip install pipenv setuptools && pip install --upgrade pipenv

COPY . /src/be/

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy

EXPOSE 8080

CMD service nginx start && gunicorn -k uvicorn.workers.UvicornWorker --access-logformat '%(h)s %(l)s %(h)s %(l)s %(t)s "%(r)s" %(s)s %(T)s' --workers=1 -b 0.0.0.0:8000 app:app
