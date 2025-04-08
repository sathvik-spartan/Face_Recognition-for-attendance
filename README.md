# Folder Setup

face_recognition_attendance/    
│    
├── dataset/                         # Each subfolder = person name     
│   ├── Alice/      
│   │   ├── img1.jpg     
│   │   └── img2.jpg     
│   └── Bob/     
│       └── bob1.jpg      
│       
├── snapshots/                       # Face snapshots saved on detection        
├── attendance.csv                   # Logs all attendance       
├── .env                             # For secure email
├── gui_face_attendance.py           # ✅ DeepFace-based recognition GUI
├── report_viewer.py       
├── report_utils.py        
├── scheduler.py                     # (Coming up)
├── requirements.txt        
