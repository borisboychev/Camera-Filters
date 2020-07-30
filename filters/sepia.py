import cv2

capture_device = cv2.VideoCapture(0)


def apply_sepia(frame, intensity=0.5):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    return frame


while True:

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    ret, frame = capture_device.read()

    sepie = apply_sepia(frame)

    cv2.imshow('sepia', sepie)
