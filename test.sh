#!/bin/bash
addr=hostname -I;
server=$1
while true; do
    
    if ping -c 4 -W 1 $server > /dev/null; then
        echo "sending data to $server"
        if who; then
            curl -X POST $server \
                -H "Content-Type: application/json" \
                -d '{"address": "$addr", "online": true}'
        fi
    else 
        echo "$server is Unreachable" 
    fi
    sleep 60
done