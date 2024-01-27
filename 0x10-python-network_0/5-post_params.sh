#!/usr/bin/env bash
# POST request with variables
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
