#!/usr/bin/env sh
set -eu

if [ "$USE" = "local" ]; then
  echo "Specified local usage, using local config"
  envsubst '${DOMAIN_NAME}' </etc/nginx/conf.d/nginx.conf.template_local >/etc/nginx/conf.d/nginx.conf
else
  envsubst '${DOMAIN_NAME}' </etc/nginx/conf.d/nginx.conf.template >/etc/nginx/conf.d/nginx.conf
fi
exec "$@"
