#!/bin/bash

SOURCE_DIR="$1"
DEST_DIR="$2"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Source directory does not exist."
  exit 1
fi

mkdir -p "$DEST_DIR"


BACKUP_FILE="$DEST_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" .

echo "Backup of $SOURCE_DIR completed successfully at $BACKUP_FILE."
