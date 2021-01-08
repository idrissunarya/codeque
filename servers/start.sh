#!/usr/bin/env bash

# start nginx
sudo nginx

# start uwsgi
uwsgi --ini /Users/idris/vps/codeque/servers/codeque_uwsgi.ini