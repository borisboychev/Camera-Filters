import cv2

capture_device = cv2.VideoCapture(0)


def make_1080p():
    capture_device.set(3, 1920)
    capture_device.set(4, 1080)


make_1080p()

while True:

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    ret, frame = capture_device.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Black&White', gray)

cv2.destroyAllWindows()