#!/bin/sh
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku container:login
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME