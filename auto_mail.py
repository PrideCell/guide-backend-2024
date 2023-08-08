import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Email parameters
smtp_server = "smtp.gmail.com"  # Your SMTP server
smtp_port = 587  # Your SMTP port
smtp_username = "guideproject2023@gmail.com"
sender_email = "guideproject2023@gmail.com"
sender_password = "ofykzotalcvaulbm"
subject = "Guide Portal Status"
message = f'''
Hello Students,
The Guide portal bugs have been fixed and has been made available for all globally. 
Kindly, register your team if not done yet.


Note:
1) This mail is sent to team leads only (Typically, 1st member of team is considered lead)
2) Kindly, read the rules mentioned on the pop-up when you click register on home page and then login.
3) In case you're not receiving the OTP/verification link kindly for 5 minutes as server may get clogged up due to high requests.
4) The team ID sent via mail will be applicable from next review onwards. For logging in to the portal use the teamID sent in mail and for rest of the cases consider Excel teamID as final for 1st review. 
5) Any Queries kindly mail us with proper subject and body. Before sending us mail double check your process.
'''



excel_file = 'Team-2023-08-05.xls'
df = pd.read_excel(excel_file)

# Get the email addresses from the "student_1_email" column
# recipients = df['student_1_email'].tolist()
recipients = ['hariharanbp6@gmail.com', 'bphariharan1301@gmail.com']

print('Type of recipients var: ', type(recipients))
# for recipient in recipients:
#     print(recipient)

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
# msg['To'] = ','.join(recipients)
msg['Bcc'] = ','.join(recipients)
msg['Subject'] = subject

# Attach the message body
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Initiate TLS connection
    server.starttls()

    # Login to the sender's email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipients, msg.as_string())
    # server.sendmail(sender_email, 'hariharanbp6@gmail.com', msg.as_string())

print("Email sent successfully")

