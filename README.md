# INTRUDER-DETECTION-SYSTEM

# 🔐 Intruder Detection System with Email Alert

This project is a **Python-based Intruder Detection System** using OpenCV and SMTP. It uses motion detection through a webcam to detect unauthorized access and sends an alert email with an attached snapshot of the intruder.

---

## 🚀 Features

- 🔑 **Password protection** before the program starts
- 🎥 **Webcam-based motion detection**
- 📷 Automatically captures image when motion is detected
- 📧 Sends **email alert** with the snapshot of the intruder
- 🛑 Program exits after correct password is entered

---

## 🛠️ Technologies Used

- Python 3.x
- OpenCV
- SMTP (for email alerts)
- EmailMessage (for email formatting)

---

## 📂 File Structure
IDS/
│
├── main.py # Main script for intruder detection
├── README.md # Project documentation
├── requirements.txt # Python dependencies (optional)
└── snap.jpg # Intruder snapshot (captured during runtime)


---

## 🔧 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/v1v8k/INTRUDER-DETECTION-SYSTEM.git
cd INTRUDER-DETECTION-SYSTEM

2. **Install dependencies**
pip install opencv-python

3. **Edit your email credentials**
  * Replace the sender_email and app_password with your Gmail and App Password.
  * Add the desired recipients in the receiver_email list.

▶️ How to Run
    python main.py
![Screenshot 2025-05-17 223221](https://github.com/user-attachments/assets/6ee770e9-12fb-45dd-b13a-5642acbc304f)
![Screenshot 2025-05-17 223257](https://github.com/user-attachments/assets/0e1fa418-3ff2-4b2d-b6cc-44a06382e329)

* Enter the correct password when prompted.
* If incorrect password is entered 3 times, the system activates.
* When motion is detected, it:
    * Highlights the intruder in the webcam feed.
    * Captures a snapshot.
    * Sends it to the configured email addresses.

🛡️ Security Note
⚠️ Never hardcode real email passwords or sensitive data in code.
For real-world deployment:

    Use .env files to store credentials.

    Implement more robust authentication mechanisms.

📷 Sample Output
<img width="710" alt="image" src="https://github.com/user-attachments/assets/ab10a929-7c6e-4a1b-8d2a-f44afb3c3d34" />

✍️ Author
Vivek Kumar – GitHub

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.


---

Let me know if you want me to generate a `requirements.txt` file or add environment variable support for passwords (`.env` file).
