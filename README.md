# keylogger.py
### Setup Instructions:

1. **Install Required Libraries:**
```bash
pip install keyboard
```

2. **Configure Gmail:**
   - Enable 2-factor authentication on your Gmail account
   - Generate an App Password:
     - Go to Google Account settings
     - Navigate to Security → 2-Step Verification → App passwords
     - Generate a new app password for "Mail."
     - Use this password in the script

3. **Update Configuration:**
   - Replace `your_email@gmail.com` with your Gmail address
   - Replace `your_app_password` with your Gmail app password
   - Replace `recipient@example.com` with the recipient's email address

4. **Run the Keylogger:**
```bash
python keylogger.py
```

### Features:
- Logs all keystrokes, including special keys
- Sends email reports every 35 seconds
- Handles special keys (Enter, Space, Backspace, etc.)
- Threaded email sending to avoid blocking keylogging
- Shows timestamp in email reports
- Sends final report when stopped

### Important Notes:
1. **Permissions:** On some systems, you might need to run with administrator privileges
2. **Gmail App Password:** Use app password instead of regular Gmail password
3. **Email Frequency:** Adjust `SEND_INTERVAL` to change how often emails are sent
4. **Security:** Keep your app password secure and don't commit it to version control

### How to Create App Password:
1. Go to your Google Account
2. Navigate to Security → 2-Step Verification → App passwords
3. Select "Mail" as the app
4. Generate the password
5. Use this password in the script

This keylogger will run in the background and send email reports with all keystrokes captured during the reporting
interval. The email reports include timestamps and the total number of keystrokes for easy tracking.
