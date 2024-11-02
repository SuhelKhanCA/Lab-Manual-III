#!/bin/bash


PATTERN="$1"
FILENAME="$2"

if [ ! -f "$FILENAME" ]; then
  echo "File does not exist."
  exit 1
fi

grep "$PATTERN" "$FILENAME"
