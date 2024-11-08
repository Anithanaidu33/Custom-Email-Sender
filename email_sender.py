import sendgrid
from sendgrid.helpers.mail import Mail
from config import Config

def send_email(to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=Config.SENDGRID_API_KEY)
    message = Mail(
        from_email='your-email@example.com',
        to_emails=to_email,
        subject=subject,
        html_content=content)
    try:
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(e.message)
        return None
