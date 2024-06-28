import random
import smtplib

def send_otp_via_email(email):
    otp = random.randint(100000, 999999)
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    message = f"Your OTP is {otp}"
    server.sendmail('your_email@example.com', email, message)
    server.quit()
    return otp

def verify_otp(user_otp, real_otp):
    return user_otp == real_otp

email = 'user@example.com'
otp = send_otp_via_email(email)
user_otp = int(input("Enter the OTP sent to your email: "))
if verify_otp(user_otp, otp):
    print("OTP verified successfully!")
else:
    print("Invalid OTP!")
