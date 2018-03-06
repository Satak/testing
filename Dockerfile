FROM alpine
ENV TAG $TAG
RUN apk add --no-cache build-base && apk add --no-cache python3 python3-dev postgresql-dev && pip3 install --upgrade pip && pip3 install virtualenv && apk add --no-cache curl

COPY ["requirements.txt", "src/", "/srv/"]
RUN virtualenv /srv/env && /srv/env/bin/pip install -r /srv/requirements.txt

WORKDIR /srv
EXPOSE 8080
USER nobody

CMD ["/srv/env/bin/gunicorn", "-b", "0.0.0.0:8080", "-w", "10", "main:app"]