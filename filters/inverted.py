import cv2

capture_device = cv2.VideoCapture(0)


def apply_invert(frame):
    return cv2.bitwise_not(frame)


while True:

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    ret, frame = capture_device.read()

    inverted = apply_invert(frame)

    cv2.imshow('inverted', inverted)
    # cv2.imshow('normal', frame)

capture_device.release()
cv2.destroyWindow()