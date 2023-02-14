#!/usr/bin/bash

source .env 
rm -r models/* 
docker-compose -f docker-compose.train.yml build
docker-compose -f docker-compose.train.yml up 
