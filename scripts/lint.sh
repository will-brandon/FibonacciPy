#!/bin/bash

docker run --rm -it -v ./src:/mnt/src -e ARGV="$*" jun-py-formatter:1.0
