FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R root:root /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts # run.sh will have executable permissions to be run as part of container.

ENV PATH="/scripts:$PATH"

CMD ["run.sh"]
