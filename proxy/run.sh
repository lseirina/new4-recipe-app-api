#!/bin/sh

set -e

# this command takes a template file, replaces any environment variable placeholders
# with their actual values, and writes he output to the 2-d file, file used by Nginx.
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
# starts the Nginx web server
nginx -g 'daemon off;' # This option tells Nginx to run in the foreground instead of as a background daemon. For Docker it is necessary for the container to keep running