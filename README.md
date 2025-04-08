# 👁️‍🗨️ Face Recognition Attendance System

A complete Python-based attendance system using DeepFace for face recognition, Tkinter GUI for real-time tracking and reporting, with automated daily email reports at 6:00 PM.

---

## 🚀 Features

- 🎥 Real-time face detection with webcam
- 🧠 DeepFace face recognition
- 🗂️ Dataset builder via webcam capture
- 📅 Attendance logging with date/time/snapshot
- 📊 Report viewer with filters, charts, and Excel export
- ✉️ Email reports (manual & scheduled)
- ⏰ Auto-email scheduler at 18:00 (configurable)

---

## 🛠 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

If you're on Linux and have issues with `tkinter`, try:
```bash
sudo apt-get install python3-tk
```

---

## 🧪 1. Capture Face Dataset

Run the face capture script:
```bash
python capture_faces.py
```
Instructions:
- Enter person's name
- Press `c` to capture face
- Press `q` to quit

Images will be saved to `dataset/Person_Name/`

---

## 🎦 2. Run Attendance GUI

Launch the real-time face recognition system:
```bash
python gui_face_attendance.py
```
This will:
- Detect faces
- Match using DeepFace
- Log attendance in `attendance.csv`
- Save snapshots in `snapshots/`

---

## 📈 3. View Reports

Open the report viewer GUI:
```bash
python report_viewer.py
```
Features:
- Filter by name and date
- Export to Excel
- View charts (attendance per person)
- Email filtered report manually

---

## 📬 4. Schedule Daily Report Email (18:00)

### 🧾 Configure `.env`
Create a file named `.env`:
```env
EMAIL_TO=receiver@example.com
EMAIL_USER=you@example.com
EMAIL_PASS=your_app_password
```

### 📆 Start Scheduler
```bash
python scheduler.py
```
This will send today's attendance report every day at 18:00.

---

## 🧠 How It Works

1. **Face Dataset** is created by capturing face images with labels.
2. **GUI starts webcam feed** and uses DeepFace to detect & recognize faces.
3. **Attendance is logged** into a CSV file with timestamps and snapshots.
4. **Reports can be viewed** via a GUI with filtering and charts.
5. **Emails are sent** daily with the day's report at 18:00 using credentials from `.env`.

DeepFace compares facial embeddings to identify matches using powerful backends like **Facenet, VGG-Face, ArcFace**, etc.

---

## 📂 Project Structure
```
face_recognition_attendance/
├── dataset/             # Face images by name
├── snapshots/           # Captured attendance snapshots
├── attendance.csv       # Attendance log
├── .env                 # Email credentials
├── capture_faces.py     # Dataset builder
├── gui_face_attendance.py
├── report_viewer.py     # Report GUI
├── report_utils.py      # Charting + email logic
├── scheduler.py         # Daily email script
└── requirements.txt
```

---

## 💡 Future Add-ons
- 🌐 Flask/Django web dashboard
- 📱 Mobile version or PWA
- 📁 Cloud storage integration

---

## 📣 License
Open-source for educational and non-commercial use.

---

## 🙌 Credits
Built with 💙 using Python, DeepFace, Tkinter, and Matplotlib.

