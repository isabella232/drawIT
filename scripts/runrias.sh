#!/usr/bin/env bash

if [ ! -z "$1" ]
then
   if [ ! -z "$2" ]
   then
      python3 ../drawit.py -mode batch -region us-south -key $1 -account $2
   else
      python3 ../drawit.py -mode batch -region us-south -key $1
   fi
fi
