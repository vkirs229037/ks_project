#!/bin/sh

if [ $# -lt 1 ]; then
    python ./main.py;
elif [ $1 != "net" ] || [ $# -gt 2 ]; then
    echo "./run.sh [net]"
else
    python ./main.py net;
fi