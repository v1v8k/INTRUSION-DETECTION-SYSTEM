import cv2
import time
import smtplib
import mimetypes
from email.message import EmailMessage

# Password Protection
correct_password = "Password0!"
max_attempts = 3
attempts = 0

# Flag to track if the correct password was entered
password_correct = False

# Password prompt with attempt limitation
while attempts < max_attempts:
    entered_password = input("Enter the password: ")
    
    if entered_password == correct_password:
        print("Password correct! Thank you for login...")
        password_correct = True
        break
    else:
        attempts += 1
        print(f"Incorrect password! Please try again")
        
    if attempts == max_attempts:
        print("Sorry you enter incorrect password.")

if password_correct:
    exit()

 
sender_email = "vivek7061054537@gmail.com" 
receiver_email = ["hyckerseeyou0@gmail.com"]  # Add additional emails here


app_password = "bjwl hofl zqit zjbr"  # Replace with your actual app password
 
cap = cv2.VideoCapture(0) 

time.sleep(2)

if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

motion_detector = cv2.createBackgroundSubtractorMOG2()

msg = EmailMessage()
msg['Subject'] = 'Alert!'
msg['From'] = sender_email
msg['To'] = ",".join(receiver_email)  
msg.set_content("Hello! \nThis is a security alert....")


sent_msg_count = 1

last_capture_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture video frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 31), 0)

    mask = motion_detector.apply(gray)

    threshold = cv2.threshold(mask, 20, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2)

    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, "Intruder Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    current_time = time.time()
    if current_time - last_capture_time >= 5: 
        img_name = "snap.jpg"
        cv2.imwrite(img_name, frame)

        with open(img_name, 'rb') as f:
            file_data = f.read()
            file_type, _ = mimetypes.guess_type(f.name)
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=f.name)

            if sent_msg_count <= 3:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(sender_email, app_password)
                    smtp.send_message(msg)
                    sent_msg_count += 1
                    print("Email Sent")
            else:
                break

        last_capture_time = current_time

    cv2.imshow("Video Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
