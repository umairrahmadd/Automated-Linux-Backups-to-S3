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


<br> Provide your Access Key, Secret Key, default region, and output format.<br>
  
<br><img width="550" height="100" alt="image" src="https://github.com/user-attachments/assets/304b0c64-66de-4345-9056-fd90484c977f" /><br>

### 3.	Create Backup Script
<img width="250" height="63" alt="image" src="https://github.com/user-attachments/assets/f44746dc-5842-4632-9f7f-aa5b3e93a042" />

### Backup Script:

<img width="1514" height="448" alt="image" src="https://github.com/user-attachments/assets/99d04e59-5a14-4a70-866d-38efc10f007d" />

<br>  This script creates a timestamped local backup and optionally uploads it to AWS S3 while maintaining a log.<br>

  ### 4.	Automate with Cron
  <img width="250" height="53" alt="image" src="https://github.com/user-attachments/assets/ed3cd71a-f265-4e77-9391-90b0ecc4dd24" />

<br> Add entry every minute:<br>

  <img width="350" height="59" alt="image" src="https://github.com/user-attachments/assets/3ef8fdad-da4e-4756-83f9-f7de6668bbe1" />

### 5. Test File for Backup Validation
<img width="350" height="70" alt="image" src="https://github.com/user-attachments/assets/2aacc65e-d73a-4902-8c8b-4c136d15e83d" />


<br>	This file (file.txt) is used to verify that the backup script correctly stores data locally and synchronizes it with Amazon S3.<br>

### 6. Local Backup Directory (Ubuntu Terminal):
<img width="350" height="60" alt="image" src="https://github.com/user-attachments/assets/29068d7b-ee5e-41cf-81b2-8b79b8f1eee9" />

<br>	The screenshot shows the ~/backup directory on the Ubuntu system. A timestamped folder named backup_2026-01-27_16-11-01 is visible, which confirms that the backup script successfully created a local copy of the source data.<br>

## Amazon S3 Bucket (AWS Management Console):
<img width="940" height="275" alt="image" src="https://github.com/user-attachments/assets/352d9e70-0c1d-4dde-814b-0af49fa379e9" />

<br> The screenshot displays the contents of the S3 bucket named aws-backups-475739. A folder named backup_2026-01-27_16-11-01/ is present, corresponding to the local backup created earlier.<br>

# VS Code GUI → S3 Integration

 ### 1. Frontend
- index.html → Dashboard layout with buttons

- style.css → Modern styling with gradients and animations

- app.js → Handles actions (backup, log, upload, clear output)

### 2. Backend (Flask)
<br>File: gui/app.py<br>  
Routes:

- / → Loads dashboard

- /backup → Runs local backup

- /log → Displays backup log

- /upload → Uploads backups to S3

### 3. Configure AWS CLI
   <img width="250" height="80" alt="image" src="https://github.com/user-attachments/assets/57b8dd90-101a-4af1-8023-90dc7f03ebfb" />

   <br> Provide your Access Key, Secret Key, default region, and output format.<br>

<br><img width="550" height="100" alt="image" src="https://github.com/user-attachments/assets/304b0c64-66de-4345-9056-fd90484c977f" /><br>

### 4. Run Flask in your VS Code Terminal:
<img width="250" height="60" alt="image" src="https://github.com/user-attachments/assets/01153b3b-4f7c-4795-a737-2344d4b57225" />

### 5. Accessing the GUI: 
Open a browser and go to http://127.0.0.1:5000. The Backup Dashboard will appear, allowing you to:
-	Run local backups
-	View backup logs
-	Upload backups to AWS S3

  <b>Purpose:<b> This section demonstrates that the application is functional and accessible via a web interface, making it easy for users to interact with the backup system

<br><img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/3bb25815-0ba5-4377-a070-93546f579d08" /><br>

### Run local backups

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/64a5ec50-a4d0-4301-a377-983d5976a131" />

### View backup logs

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/0645eae1-2762-410c-bf58-40e3f10524e6" />

### Upload backups to AWS S3

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/c6b78e90-4a08-4dee-8774-3de369a82d15" />

### Verifying

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/79b1cf07-5f92-48e1-9f08-b915c1c46fa3" />

- A new backup is created and is uploaded to S3.






  



