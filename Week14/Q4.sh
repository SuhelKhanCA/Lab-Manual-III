#!/bin/bash

# Variables
LOG_DIR="/var/log/myapp"
ARCHIVE_DIR="/var/log/myapp/archive"
DAYS_TO_KEEP=30

# Create directories if they do not exist
mkdir -p $ARCHIVE_DIR

# Rotate logs
find $LOG_DIR -type f -name "*.log" -exec mv {} $ARCHIVE_DIR/ \;

# Archive and compress old logs
find $ARCHIVE_DIR -type f -name "*.log" -mtime +$DAYS_TO_KEEP -exec rm {} \;

# Print success message
echo "Log rotation and cleanup completed. Old logs older than $DAYS_TO_KEEP days are deleted."
