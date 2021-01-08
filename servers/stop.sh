#!/usr/bin/env bash

# shut down uwsgi
uwsgi --stop /Users/idris/vps/codeque/codeque/codeque.pid

# gracefully stop nginx
sudo nginx -s stop