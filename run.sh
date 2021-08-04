#!/bin/sh

FILE=".envrc"
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist, ask Alex where to get it"
    exit 1
fi

#curl -X POST -H 'Content-type: application/json' --data '{"text":"start Candice prog"}' $SLACK_WEBHOOK
#rm -rf screenshot/*.png

node index.js 0
node index.js 1
node index.js 2
node index.js 3
python3 send_email.py #-r 'alozz1991@gmail.com'
