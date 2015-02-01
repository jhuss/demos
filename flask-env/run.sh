#!/bin/sh
# flask & env demo
# author: Jesús Jerez <jerezmoreno@gmail.com>


DIR="$( cd "$( dirname "$0" )" && pwd )"
source "$DIR/.env"

uwsgi --http $SERVER_HOST:$SERVER_PORT --wsgi-file "$DIR/wsgi.py" --callable application
