#!/bin/bash

# Variables
BACKUP_DIR="/var/backups"
CRITICAL_FILES="/etc/passwd /etc/shadow"
USER_TO_ADD="newuser"

# Create backup directory if it doesn't exist
sudo mkdir -p $BACKUP_DIR

# Backup critical files
sudo cp $CRITICAL_FILES $BACKUP_DIR/

# Add a new user and set permissions
sudo useradd $USER_TO_ADD
sudo passwd $USER_TO_ADD

# Modify permissions
sudo chown $USER_TO_ADD:$USER_TO_ADD $BACKUP_DIR/*
sudo chmod 600 $BACKUP_DIR/*

echo "User $USER_TO_ADD added and critical files backed up."
