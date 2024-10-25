#!/bin/bash

greet_user() {
  echo "Hello, $1! Welcome to the shell scripting world."
}

echo "Enter your name:"
read user_name

greet_user "$user_name"
