import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load data from Excel file
data = pd.read_excel("Team.xls")  # Replace "input.xlsx" with your file path

# Email configuration
smtp_server = "smtp.gmail.com"  # Your SMTP server
smtp_port = 587  # Your SMTP port
smtp_username = "guideproject2023@gmail.com"
smtp_password = "rceddrndzxncxiuw"
sender_email = "guideproject2023@gmail.com"

# Create SMTP connection
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
smtp.login(smtp_username, smtp_password)

# Send emails
for index, row in data.iterrows():
    subject = "Team Registration Confirmation"
    team_id = row["teamID"]
    
    if str(row["no_of_members"])== 2:
        recipients = [
            row["student_1_email"], 
            row["student_2_email"], 
        ]
        name_1 = row["student_1_name"]
        name_2 = row["student_2_name"]
        message = f'''Hello {name_1} and {name_2}!
    This is another confirmation regarding your team's registration for your final year project. Your updated team ID is {team_id}.
        
    You have to use the updated teamID as username from now on to login and access your profile. Please note that we're working on some bug fixes and the site will be in maintenance until Monday Afternoon.
        
    Any queries, please feel free to mail us.

    Note: 
    1) If your Team mate has not recieved it don't worry it is only being sent to 1st member of the team.
    2) Kindly, ignore 1st point if you don't have a team member.
        
    Thank You
        
    Warm Regards,
    Pride Cell
    '''
    else:
        recipients = [row["student_1_email"],]
        name_1 = row["student_1_name"]
    
        message = f'''Hello {name_1}!
    This is another confirmation regarding your team's registration for your final year project. Your updated team ID is {team_id}.
        
    You have to use the updated teamID as username from now on to login and access your profile. Please note that we're working on some bug fixes and the site will be in maintenance until Monday afternoon.
        
    Any queries, please feel free to mail us.

    Note: 
    1) If your Team mate has not recieved it don't worry it is only being sent to 1st member of the team.
    2) Kindly, ignore 1st point if you don't have a team member.
        
    Thank You
        
    Warm Regards,
    Pride Cell
'''

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipients[0]
    # if str(row["no_of_members"])== '2':
    #     msg["Bcc"] = recipients[1]
    #     print('BCC is: ', msg["Bcc"])
    # print(msg["To"])
    msg["Subject"] = subject

    # personalized_message = message.format(name=recipient_name)
    msg.attach(MIMEText(message, "plain"))

    smtp.sendmail(sender_email, recipients, msg.as_string())
    print(f"Email sent to {name_1} ({recipients})")

# Close SMTP connection
smtp.quit()
