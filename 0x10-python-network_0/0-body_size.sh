#!/bin/bash
# Sends a request to curl and output the response bytes
curl -s "$1" | wc -c
