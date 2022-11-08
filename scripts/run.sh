#!/usr/bin/env bash

if [ ! -z "$1" ]
then
   python3 ../drawit.py -mode batch -input ~/Documents/drawIT/$1 -output ~/Documents/drawIT
else
   python3 ../drawit.py -mode batch -input ~/Documents/drawIT/vpc-web.json -output ~/Documents/drawIT
fi

