import sys
import cv2

print(sys.executable)  # Print the Python interpreter path
print(sys.path)        # Print the list of directories where Python looks for modules

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame.")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if 47 <= hue_value <= 70:
        color = "RED"
    elif 29 <= hue_value < 45:
        color = "ORANGE"
    elif 17 <= hue_value < 20:
        color = "YELLOW"
    elif 20 <= hue_value < 35:
        color = "GREEN"
    elif 85 <= hue_value < 110:
        color = "CYAN"
    elif 110 <= hue_value <= 255:
        color = "BLUE"
    elif 130 <= hue_value < 155:
        color = "VIOLET"
    elif 7 <= hue_value <= 7:
        color = "BLACK"
    else:
        color = "UNKNOWN"


    pixel_center_bgr = frame[cy, cx]
    print(pixel_center)
    cv2.putText(frame, color, (10, 50), 0, 1, (255, 0, 0), 2)

    # Draw circle on the center
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        print("Esc key was pressed.")
        break
cap.release()
cv2.destroyAllWindows()
