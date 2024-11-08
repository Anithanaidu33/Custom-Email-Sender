# Custom-Email-Sender
This project is a custom email-sending application that allows users to send personalized emails using a Google Sheet or CSV file for data input. It includes features like email scheduling, throttling, tracking, and real-time analytics.

Features
Import email data from Google Sheets or CSV files
Connect email accounts using OAuth2 or SMTP
Customize email content with dynamic fields
Schedule and throttle email sending
Track delivery statuses using SendGrid
Real-time dashboard with analytics on sent emails
Technologies Used
Backend: Flask
Task Queue: Celery (with Redis as the broker)
Database: SQLAlchemy
Email Service Provider (ESP): SendGrid
Frontend: HTML/CSS for the dashboard
Prerequisites
Python 3.7+
Redis (for Celery task queue)
A SendGrid account for email sending and tracking
Installation
Clone the repository:


git clone https://github.com/your-username/Custom-Email-Sender.git
cd Custom-Email-Sender
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Set up Redis (required for Celery):

Install Redis and start the server locally, or use a hosted Redis service.
Configuration
Create a .env file in the project root with the following environment variables:

SECRET_KEY=your-secret-key
GOOGLE_SHEET_ID=your-google-sheet-id
SENDGRID_API_KEY=your-sendgrid-api-key
DATABASE_URL=sqlite:///emails.db
REDIS_URL=redis://localhost:6379/0
Obtain API keys and IDs:

SendGrid: Create an account on SendGrid and generate an API key.
Google Sheets: Follow the steps to set up Google Sheets API access.
Database Initialization
Initialize the database to store email statuses.

Set up the database:

flask db init
flask db migrate
flask db upgrade
Running the Application
Start the Celery worker (for scheduling and sending emails):


celery -A tasks.celery worker --loglevel=info
Run the Flask application:


flask run
Access the dashboard by navigating to http://127.0.0.1:5000 in your web browser.

Usage
Upload Data: Use the Google Sheets or CSV upload option to import recipient data, such as email addresses and dynamic fields.
Create Custom Emails: Enter a customizable prompt with placeholders (e.g., {Company Name}, {Location}) that will be replaced with data from each row.
Schedule Emails: Choose scheduling options to send emails immediately or at specified intervals.
View Real-Time Analytics: Track email statuses (Sent, Scheduled, Failed) and delivery statuses (Delivered, Opened, Bounced) on the dashboard.

Project Structure

Custom-Email-Sender/
│
├── app.py                     # Main application file
├── config.py                  # Configuration file for settings
├── requirements.txt           # Project dependencies
├── static/
│   └── css/
│       └── styles.css         # Styling for the dashboard
├── templates/
│      dashboard.html         # HTML for the dashboard
├── tasks.py                   # Celery tasks for email scheduling
├── email_sender.py            # Email handling logic
├── database.py                # Database models
├── README.md                  # Project documentation
└── .env                       # Environment variables for sensitive info
Testing
Test email sending and tracking features by configuring a limited test dataset.
Ensure scheduled emails are sent at the expected times and throttling is respected.
Deployment
To deploy the application:

Set up a production-ready database (e.g., PostgreSQL).
Use a production-ready server (e.g., Gunicorn) to run the Flask app.
Configure Redis on a hosted service for Celery.
Host the app on a cloud provider (e.g., AWS, DigitalOcean).


License
This project is licensed under the MIT License.
