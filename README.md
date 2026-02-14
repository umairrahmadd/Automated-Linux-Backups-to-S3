# Automated Linux Backups to S3 + Flask GUI
## 📌 Overview

This project provides a complete solution for automated backups:

- Local backups with timestamped folders

- Synchronization with Amazon S3

- Logging of backup operations

- A Flask GUI dashboard (HTML, CSS, JavaScript) for easy interaction

## ⚙️ Setup Instructions

   ### 1. Install AWS CLI
<img width="250" height="80" alt="image" src="https://github.com/user-attachments/assets/b8f080cb-88c1-4b40-881a-4eae4e38908e" />

### 2. Configure AWS CLI
<img width="250" height="80" alt="image" src="https://github.com/user-attachments/assets/c814f67e-80b1-4b58-91f8-f314573dc880" />


- Provide your Access Key, Secret Key, default region, and output format.
  
<img width="550" height="100" alt="image" src="https://github.com/user-attachments/assets/304b0c64-66de-4345-9056-fd90484c977f" />

### 3.	Create Backup Script
<img width="250" height="63" alt="image" src="https://github.com/user-attachments/assets/f44746dc-5842-4632-9f7f-aa5b3e93a042" />

### Backup Script:

<img width="1514" height="448" alt="image" src="https://github.com/user-attachments/assets/99d04e59-5a14-4a70-866d-38efc10f007d" />

-	This script creates a timestamped local backup and optionally uploads it to AWS S3 while maintaining a log.

  ### 4.	Automate with Cron
  <img width="250" height="53" alt="image" src="https://github.com/user-attachments/assets/ed3cd71a-f265-4e77-9391-90b0ecc4dd24" />

- Add entry every minute:

  <img width="350" height="59" alt="image" src="https://github.com/user-attachments/assets/3ef8fdad-da4e-4756-83f9-f7de6668bbe1" />

### Test File for Backup Validation
<img width="350" height="70" alt="image" src="https://github.com/user-attachments/assets/2aacc65e-d73a-4902-8c8b-4c136d15e83d" />


•	This file (file.txt) is used to verify that the backup script correctly stores data locally and synchronizes it with Amazon S3.

### Local Backup Directory (Ubuntu Terminal):
<img width="350" height="60" alt="image" src="https://github.com/user-attachments/assets/29068d7b-ee5e-41cf-81b2-8b79b8f1eee9" />

-	The screenshot shows the ~/backup directory on the Ubuntu system. A timestamped folder named backup_2026-01-27_16-11-01 is visible, which confirms that the backup script successfully created a local copy of the source data.




