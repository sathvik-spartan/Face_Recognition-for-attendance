import pandas as pd
import schedule
import time
from datetime import datetime
from report_utils import send_report_email
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

EMAIL_TO = os.getenv("EMAIL_TO")  # your recipient email from .env
CSV_FILE = "attendance.csv"

def send_daily_report():
    try:
        df = pd.read_csv(CSV_FILE)
        today = datetime.now().strftime("%Y-%m-%d")
        today_df = df[df["Date"] == today]

        if today_df.empty:
            print(f"[{today}] No attendance records to send.")
            return

        send_report_email(EMAIL_TO, today_df)
        print(f"[{today}] ✅ Attendance report sent to {EMAIL_TO}")
    except Exception as e:
        print(f"[ERROR] Failed to send report: {e}")

# Schedule job at 18:00 every day
schedule.every().day.at("18:00").do(send_daily_report)

print("[SCHEDULER] Running... Waiting for 18:00 daily report...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
