#!/bin/bash
# sends a GET request to the URL with header variable
curl -s -H "X-School-User-Id: 98" "$1"
