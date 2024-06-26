import os
import random
import smtplib
from email.mime.text import MIMEText


# Function to generate OTP (6 digit)

def generate_otp():

    return ''.join(random.choices('0123456789', k=6))

# Function to send OTP to user's email address
# the sender email and password are retrieved from environment variables(OS) SENDER_EMAIL and SENDER_PASSWORD...
# ,this keeps sensitive data out of the code itself.

def send_otp_email(email, otp):

    sender_email = os.environ.get('SENDER_EMAIL')
    sender_password = os.environ.get('SENDER_PASSWORD')


    if sender_email is None or sender_password is None:
        print("Sender email or password not set. Please set environment variables SENDER_EMAIL and SENDER_PASSWORD.")
        return

    message = MIMEText(f"Your OTP is: {otp}")
    message['Subject'] = 'OTP Verification'
    message['From'] = sender_email
    message['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("OTP sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP. Error: {e}")


# Function to prompt user to enter OTP

def enter_otp():
    return input("Enter the OTP sent to your email: ")


# Function to verify OTP

def verify_otp(otp, entered_otp):
    return otp == entered_otp



# Main function

def main():
    email = input("Enter your email address: ")

    # Generate OTP and send it to the user's email

    otp = generate_otp()
    send_otp_email(email, otp)

    # Prompt user to enter OTP

    entered_otp = enter_otp()

    # Verify OTP

    if verify_otp(otp, entered_otp):
        print("OTP verification successful. Access granted.")
    else:
        print("OTP verification failed. Access denied.")

        # allowing user to retry OTP entry
        retry = input("Do you want to retry? (yes/no): ")
        if retry.lower() == 'yes':
            main()
        else:
            print("Exiting program.")



if __name__ == "__main__":
    main()
