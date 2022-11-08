#!/usr/bin/env bash

if [ ! -z "$1" ]
then
   python3 ../drawit.py -mode batch -split combine -layout horizontalnolink -input ~/Documents/drawIT/$1 -output ~/Documents/drawIT
else
   python3 ../drawit.py -mode batch -split combine -layout horizontalnolink -input ~/Documents/drawIT/slz-vsi.json -output ~/Documents/drawIT
fi

