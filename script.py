import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to send email with optional attachment
def send_email(sender_email, sender_password, receiver_email, subject, body, attachment=None):
    try:
        # Setup the MIME (Multipurpose Internet Mail Extensions)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file if provided
        if attachment:
            # Open the file in binary mode
            with open(attachment, "rb") as file:
                # MIMEBase helps attach the file
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)

                # Add the header to the attachment
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')

                # Attach the file to the message
                msg.attach(part)

        # Establish connection with the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Google's SMTP server for sending emails
        server.starttls()  # Secure the connection

        # Log in to the SMTP server
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

        print(f"Email sent successfully to {receiver_email}.")

        # Close the connection
        server.quit()

    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")

# Main function to run the script
def main():
    # Replace these variables with your details
    sender_email = input("Enter your email address: ")  # Sender's email address (e.g., username@university.ac.in)
    sender_password = input("Enter your password: ")  # Password or App Password if 2FA is enabled

    # Input the list of recipients (comma-separated emails)
    recipients = input("Enter the recipient email addresses (comma-separated): ").split(',')
    recipients = [email.strip() for email in recipients]  # Clean any extra spaces

    subject = input("Enter email subject: ")  # Subject of the email
    body = input("Enter email body: ")  # Body of the email

    # Ask the user if they want to attach a file
    attachment = input("Enter file path to attach (leave blank to skip): ").strip()

    # Only pass attachment if the user provides a valid file path
    if attachment and os.path.isfile(attachment):
        for recipient in recipients:
            send_email(sender_email, sender_password, recipient, subject, body, attachment)
    else:
        for recipient in recipients:
            send_email(sender_email, sender_password, recipient, subject, body)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
