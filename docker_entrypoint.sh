#!/bin/bash

HOSTNAME=$1
IP=$(dig +short "$HOSTNAME"| tail -n 1)
if [ ! -z "$IP"] ; then
  echo  python3 -u DRipper.py -s "$IP" -t 135 -p 443
else
  echo python3 -u DRipper.py -s "$HOSTNAME" -t 135 -p 443
fi
