#!/bin/bash
curl -I http://mercury.picoctf.net:53554/index.php | grep pico | awk -F': ' '{print $2}'
