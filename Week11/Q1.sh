#!/bin/bash

echo "Enter the file name:"
read file_name

if [ -e "$file_name" ]; then
  echo "The file '$file_name' exists."
else
  echo "The file '$file_name' does not exist."
fi
