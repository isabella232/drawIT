#!/usr/bin/env bash

if [ ! -z "$1" ]
then
   python3 ../drawit.py -mode batch -key $1
else
   python3 ../drawit.py -mode gui
fi
