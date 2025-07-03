
# 🔐 Intrusion Detection System with Email Alert

This project is a **Python-based Intrusion Detection System** using OpenCV and SMTP. It uses motion detection through a webcam to detect unauthorized access and sends an alert email with an attached snapshot of the intruder.

---

## 🚀 Features

- 🔑 **Password protection**
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

## 🔧 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/v1v8k/INTRUSION-DETECTION-SYSTEM.git
cd INTRUSION-DETECTION-SYSTEM

```
2. **Install dependencies**
```bash
pip install opencv-python
```
4. **Edit your email credentials**
  * Replace the sender_email and app_password with your Gmail and App Password.
  * Add the desired recipients in the receiver_email list.

## ▶️ How to Run
```bash
    python3 IDS.py
```

* Enter the correct password when prompted.
* If incorrect password is entered 3 times, the system activates.
* When motion is detected, it:
    * Highlights the intruder in the webcam feed.
    * Captures a snapshot.
    * Sends it to the configured email addresses.
 
## 📷 Sample 
![Screenshot 2025-05-17 223257](https://github.com/user-attachments/assets/0e1fa418-3ff2-4b2d-b6cc-44a06382e329)
![Screenshot 2025-05-17 223221](https://github.com/user-attachments/assets/6ee770e9-12fb-45dd-b13a-5642acbc304f)
<img width="481" alt="image" src="https://github.com/user-attachments/assets/98b311ab-bf76-48e8-9c65-d20724998786" />


## 🛡️ Security Note
⚠️ Never hardcode real email passwords or sensitive data in code.
For real-world deployment:

    Use .env files to store credentials.

    Implement more robust authentication mechanisms.

## 📷 Sample Output
![image](https://github.com/user-attachments/assets/09e23360-61c3-4d8d-afd0-45f64ccb8943)



✍️ Author
Vivek Kumar

---
