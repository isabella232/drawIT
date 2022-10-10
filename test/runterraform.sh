#!/usr/bin/env bash

if [ ! -z "$1" ]
then
   if [ ! -z "$2" ]
   then
      python3 ../drawit.py -mode batch -region us-south -key $1 -account $2
   else
      python3 ../drawit.py -mode batch -region us-south -key $1
   fi
else
   python3 ../drawit.py -mode terraform -tables ../terraform/tables  -input ibmvpc.json -output downloads
fi
