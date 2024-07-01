server {
    # specifies the port that Nginx will listen on for incoming HTTP requests
    listen $(LISTEN_PORT);

    # defines how Nginx should handle requests to the /static URL path
    location /static {
        # any request to /static will be served from the /vol/static directory
        alias /vol/static:
    }

    # defines how Nginx should handle all other requests (i.e., those that don't match /static).
    location / {
        # tells Nginx to forward requests to a uWSGI server
        uwsgi_pass           ${APP_HOST}:${APP_PORT}; # the hostname and port of the uWSGI
        include              /etc/nginx/uwsgi_params; # includes a file containing uWSGI parameters.
        client_max_body_size 10M; # allowed size of photo
    }
}