import cv2
import numpy

capture_device = cv2.VideoCapture(0)


def verify_alpha(frame):
    try:
        frame.shape[3]  # 4th pos
    except IndexError:
        # creates 4th pos (alpha channel)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    return frame


def apply_sepia(frame, intensity_level):
    frame = verify_alpha(frame)
    frame_height, frame_width, frame_channel = frame.shape
    #           blue,green,red,alpha
    sepia_bgra = (20, 66, 112, 1)
    overlay = numpy.full((frame_height, frame_width, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity_level, frame, 1, 0, frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame


while True:

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    ret, frame = capture_device.read()
    sepia = apply_sepia(frame, 0.3)

    cv2.imshow('sepia', sepia)


capture_device.release()
cv2.destroyWindow()