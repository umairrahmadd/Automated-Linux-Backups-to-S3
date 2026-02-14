#!/bin/bash

# Source and destination paths
src=/home/umair/mydata
dest=/home/umair/backup

# Local backup (copy folder with proper timestamp)
mkdir -p $dest
cp -r $src $dest/backup_$(date +%Y-%m-%d_%H-%M-%S)

# Upload to AWS S3
aws s3 sync $dest s3://aws-backups-475739/ --delete

# Logging
echo "Backup folder copied and succssfully uploaded to S3 at $(date '+%Y-%m-%d %H:%M:%S')" >> /home/umair/backup.log
