server {
    listen ${LISTEN_PORT};
    # requests with 'static' in url will handle here
    location /static {
        # alias заменяет часть URL запроса, a request for /static/css/styles.css will be served from /vol/static/css/styles.css
        alias /vol/static;
    }
    # handles all other requests (no static)
    location / {
        # передает серверу uWSGI, работающему на хосте и порту, указанном в переменных ${APP_HOST} и ${APP_PORT}.
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /ect/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}