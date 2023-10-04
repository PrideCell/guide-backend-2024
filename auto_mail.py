import pandas as pd
import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load data from Excel file
data = pd.read_excel("mailing_peeps_left.xlsx")  # Replace "input.xlsx" with your file path

# Email configuration
smtp_server = "smtp.gmail.com"  # Your SMTP server
smtp_port = 587  # Your SMTP port
smtp_username = "guideproject2023@gmail.com"
smtp_password = os.environ.get('EMAIL_HOST_PASSWORD_GMAIL')
sender_email = "guideproject2023@gmail.com"

# Create SMTP connection
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
smtp.login(smtp_username, smtp_password)
site_link = 'https://guide-portal-production.up.railway.app/accounts/login'
# Send emails
for index, row in data.iterrows():
    subject = "Team Registration Confirmation"
    team_id = row["teamID"]
    
    if str(row["no_of_members"])== '2':
        recipients = [
            row["student_1_email"], 
            row["student_2_email"], 
        ]
        name_1 = row["student_1_name"]
        name_2 = row["student_2_name"]
        message = f'''Hello {name_1} and {name_2}!
    You have been registered with the guide portal for your final year project. 
    Your team ID is {team_id}.
    Login to the portal {site_link}
    Username : TeamID
    Password : qWERTY123!@#

    Kindly follow the points without fail and mail us incase of queries
    1.Reset your password using the reset link which can be found in the portal
    2.Some details currently associated with your team are mere placeholders.
    3.Edit the project domain, description, phone numbers and any other details which seem inaccuarte.
    

    Regards  
    Pride Cell
    '''
    else:
        recipients = [row["student_1_email"],]
        name_1 = row["student_1_name"]
    
        message = f'''Hello {name_1}!
    You have been registered with the guide portal for your final year project. 
    Your team ID is {team_id}.
    Login to the portal {site_link}
    Username : TeamID
    Password : qWERTY123!@#

    Kindly follow the points without fail and mail us incase of queries
    1.Reset your password using the reset link which can be found in the portal
    2.Some details currently associated with your team are mere placeholders.
    3.Edit the project domain, description, phone numbers and any other details which seem inaccuarte.

    Regards
    Pride Cell

'''

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipients[0]
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    smtp.sendmail(sender_email, recipients, msg.as_string())
    print(f"Email sent to {name_1} ({recipients})")
smtp.quit()


