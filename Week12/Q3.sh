#!/bin/bash


for USERNAME in "$@"; do

  sudo useradd "$USERNAME" -m
  echo "$USERNAME:defaultpassword" | sudo chpasswd
  echo "User $USERNAME created."
done
