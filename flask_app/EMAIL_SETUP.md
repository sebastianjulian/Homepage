# Email Configuration Setup Guide

The contact form now supports sending emails directly to contact@antistrange.net. Follow these steps to configure email functionality.

## 1. Configure Email Settings

Edit the `.env` file in the flask_app directory with your email provider settings:

### For Gmail (Recommended):
```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-gmail@gmail.com
MAIL_PASSWORD=your-app-password
CONTACT_EMAIL=contact@antistrange.net
```

**Important for Gmail:**
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an "App Password" (not your regular password)
   - Go to Google Account Settings → Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
   - Use this app password in MAIL_PASSWORD

### For Outlook/Hotmail:
```env
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@outlook.com
MAIL_PASSWORD=your-password
CONTACT_EMAIL=contact@antistrange.net
```

### For Other Providers:
Check your email provider's SMTP settings and update accordingly.

## 2. Test the Setup

1. Start the Flask application:
   ```bash
   cd flask_app
   python app.py
   ```

2. Go to http://localhost:5000/contact

3. Fill out and submit the contact form

4. Check your contact@antistrange.net inbox for the message

## 3. How It Works

When someone submits the contact form:

1. **Form Submission**: JavaScript sends form data to `/api/contact`
2. **Validation**: Server validates required fields and email format
3. **Email Creation**: Flask-Mail creates an email with:
   - **Subject**: "Website Contact: Message from [Name]"
   - **To**: contact@antistrange.net
   - **Reply-To**: The sender's email address
   - **Body**: Formatted message with sender details
4. **Email Delivery**: Message is sent via your configured SMTP server
5. **Response**: Success/error message shown to user

## 4. Email Format

You'll receive emails like this:

```
From: your-smtp-email@gmail.com
To: contact@antistrange.net
Reply-To: sender@example.com
Subject: Website Contact: Message from John Doe

New message received from your website contact form:

Name: John Doe
Email: sender@example.com
Date: 2025-09-25 16:45:30

Message:
Hello! I'm interested in your astrophotography work...

---
This message was sent via the contact form on your website.
You can reply directly to this email to respond to John Doe.
```

## 5. Security Notes

- **Never commit .env files** to version control (it's in .gitignore)
- **Use app passwords** for Gmail, not regular passwords
- **Keep credentials secure** and rotate them periodically
- **Monitor email usage** to prevent spam abuse

## 6. Troubleshooting

### Common Issues:

**"Authentication failed"**
- Check username/password are correct
- For Gmail: Use app password, not regular password
- Ensure 2FA is enabled for Gmail

**"Connection refused"**
- Check MAIL_SERVER and MAIL_PORT settings
- Verify your internet connection
- Some ISPs block SMTP ports

**"Messages not received"**
- Check spam/junk folders
- Verify CONTACT_EMAIL is correct
- Test with a simple email client first

### Testing SMTP Settings:

You can test your SMTP settings using Python:

```python
import smtplib
from email.mime.text import MIMEText

# Test connection
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your-email@gmail.com', 'your-app-password')
    print("SMTP connection successful!")
    server.quit()
except Exception as e:
    print(f"SMTP connection failed: {e}")
```

## 7. Production Deployment

For production deployment:

1. **Use environment variables** on your hosting platform
2. **Set up proper logging** instead of print statements
3. **Consider rate limiting** to prevent spam
4. **Use a dedicated SMTP service** like SendGrid or Mailgun for high volume

---

**Setup completed!** Your contact form will now send emails directly to contact@antistrange.net.