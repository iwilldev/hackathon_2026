#!/bin/bash
for i in {1..10}; do
    host=cslab$i
    if ping -c 4 -W 1 $host > /dev/null; then
        echo "pinging $host"
        ping $host
    else 
        echo "Unreachable" 
    fi

done