# Mail Automation Script

## Overview

This Python script allows you to send emails to multiple recipients with optional attachments. It uses the `smtplib` and `email` libraries to send emails through an SMTP server (Gmail in this case). The script can be run in any Python environment, where the user inputs their email details, the recipients, subject, body, and optionally, a file to attach to the email.

## Features

- Send emails to multiple recipients.
- Attach files to the email (optional).
- Secure SMTP connection with TLS (Transport Layer Security).
- User-friendly prompts for inputs.

## Requirements

- Python 3.x
- Access to a Gmail account (or modify SMTP settings for other email providers).
- An app password if using Gmail with two-factor authentication (2FA).
- The `os` and `smtplib` Python libraries (standard in most Python installations).

## Setup

### 1. Install Python

Ensure you have Python 3.x installed on your system. You can download and install it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. Setting up Gmail for SMTP (if using Gmail)

If you're using Gmail and have two-factor authentication (2FA) enabled, you will need to create an app password:

1. Go to [Google Account Security Settings](https://myaccount.google.com/security).
2. Under "Signing in to Google," click on "App Passwords."
3. Generate an app password for "Mail" and "Windows Computer" (or any platform you use).
4. Use this app password instead of your Gmail account password in the script.

### 3. Modify the Script (Optional)

The script is configured to use Gmail's SMTP server (`smtp.gmail.com`) by default. If you're using a different email provider, modify the SMTP server address and port:

- For Gmail: `smtp.gmail.com`, Port: 587
- For Outlook: `smtp-mail.outlook.com`, Port: 587
- For Yahoo: `smtp.mail.yahoo.com`, Port: 587

Update these details in the `send_email()` function if needed.

## Running the Script

1. Download or clone the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Run the script by executing:

   ```bash
   python email_sender.py
