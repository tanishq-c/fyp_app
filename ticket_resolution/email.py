import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Set up the email addresses and message content
def send_email(id, cust_email, comments, status, dept_name):
    sender_email = "chatbotfyp28@gmail.com"
    receiver_email = cust_email
    subject = f"Ticket ID {id}: Update on Your Ticket Status"
    ip_body = f'''
Dear User,

We hope this email finds you well. We are writing to update you on the status of your support ticket {id}. We are pleased to inform you that your issue is currently in progress, and the ticket status has been updated to "In Progress."

Your ticket has been assigned to the {dept_name} department.

Our support team is actively working to resolve your issue, and we appreciate your patience while we work towards a resolution. Please be assured that we will keep you updated on the status of your ticket and any progress made towards resolving your issue.

If you have any questions or concerns about your ticket's progress, please don't hesitate to reach out to us. Our support team is always here to assist you.

Thank you for choosing our company, and we look forward to resolving your issue as soon as possible.

Best regards,
FYP Support Team.
'''

    com_body = f'''
Dear User,

We hope this email finds you well. We are writing to update you on the status of your support ticket {id}. We are pleased to inform you that your issue has been resolved, and the ticket status has been updated to "Completed."

Our team has made the following suggestions to resolve your issue:
{comments}

We are glad that we were able to resolve your issue, and we appreciate your patience throughout the process. If you have any further questions or concerns, please don't hesitate to reach out to us. Our support team is always here to assist you.

Thank you for choosing our company, and we look forward to serving you again in the future.

Best regards,
FYP Support Team.
'''

    rej_body = f'''
Dear User,

We hope this email finds you well. We are writing to update you on the status of your support ticket {id}. We regret to inform you that your request has been rejected, and the ticket status has been updated to "Rejected."

Our team believes that your query is invalid and cannot be resolved for the following reasons:
{comments}

We understand that this news may be disappointing, and we apologize for any inconvenience this may have caused you. Please be assured that we carefully reviewed your request and made the best decision based on the information available.

If you have any questions or concerns about the rejection of your ticket, please don't hesitate to reach out to us. Our support team is always available to help you and provide additional information.

Thank you for choosing our company, and we hope to have the opportunity to serve you again in the future.

Best regards,
FYP Support Team.
    '''
    # Create a message object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add the message body
    if status == "In-Progress":
        message.attach(MIMEText(ip_body, "plain"))
    if status == "Completed":
        message.attach(MIMEText(com_body, "plain"))
    if status == "Rejected":
        message.attach(MIMEText(rej_body, "plain"))


    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(sender_email, "abpcegugwaaflfpy")
        server.sendmail(sender_email, receiver_email, message.as_string())