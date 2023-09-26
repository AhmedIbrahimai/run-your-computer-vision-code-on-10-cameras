import cv2
import threading

# Function to perform face detection on a single camera
def detect_faces(camera_url, camera_name):
    cap = cv2.VideoCapture(camera_url)

    if not cap.isOpened():
        print(f"Error: Unable to open camera {camera_name}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Error reading frame from camera {camera_name}")
            break

        # Perform face detection on the frame here (you can use OpenCV's face detection)
        # Replace this with your actual face detection code
        # Example:
        # detected_faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        # for (x, y, w, h) in detected_faces:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with detected faces
        cv2.imshow(camera_name, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# List of IP camera URLs and camera names
camera_info = [
    {"url": "http://camera1_ip_address/video_feed", "name": "Camera 1"},
    {"url": "http://camera2_ip_address/video_feed", "name": "Camera 2"},
    # Add URLs and names for the other cameras here
]

# Create threads for each camera
threads = []
for info in camera_info:
    thread = threading.Thread(target=detect_faces, args=(info["url"], info["name"]))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
