#!/bin/bash

if(( ! -d env))
then
	virtualenv env
fi
if(( ! -f requirements.txt))
then
	pip3 install -r requirements.txt
fi
python3 ./main.py
