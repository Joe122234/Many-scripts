import cv2
import face_recognition

# Paths to images
elon_musk_image_path = "/Users/henry/Desktop/NumpyProject/faces/elonmusk.jpg"
henry_image_path = "/Users/henry/Desktop/NumpyProject/faces/Henry.png"


# Load image of Elon Musk and encode his face
elon_musk_image = face_recognition.load_image_file(elon_musk_image_path)
elon_musk_encoding = face_recognition.face_encodings(elon_musk_image)[0]

# Load image of Henry and encode his face
henry_image = face_recognition.load_image_file(henry_image_path)
henry_encoding = face_recognition.face_encodings(henry_image)[0]

# List of known face encodings and corresponding names
known_face_encodings = [elon_musk_encoding, henry_encoding]
known_face_names = ["Elon Musk", "Henry"]

# Capture video from webcam
video_capture = cv2.VideoCapture(0)

# Set camera resolution
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Width
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Height

# Display frame every nth iteration
display_interval = 3  # Display every 3rd frame
frame_count = 0

while True:
    ret, frame = video_capture.read()
    frame_count += 1
    
    if frame_count % display_interval == 0:
        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame, model="hog")
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each detected face
        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            # Compare face encoding with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            percentage = None

            # If match found, assign corresponding name and percentage
            if True in matches:
                distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                min_distance = min(distances)
                min_distance_index = distances.tolist().index(min_distance)
                name = known_face_names[min_distance_index]
                percentage = (1 - min_distance) * 100

            # Draw rectangle around the face and display name and percentage
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            text = f"{name} ({percentage:.2f}%)" if percentage is not None else name
            cv2.putText(frame, text, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
