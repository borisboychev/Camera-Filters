import cv2
import numpy

capture_device = cv2.VideoCapture(0)


def apply_blur(frame):
    blur = cv2.GaussianBlur(frame, (7, 7,), cv2.BORDER_DEFAULT)
    frame = cv2.cvtColor(blur, cv2.COLOR_BGRA2BGR)
    return frame


while True:

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    ret, frame = capture_device.read()
    blur = apply_blur(frame)

    cv2.imshow('blur', blur)

cv2.destroyAllWindows()
