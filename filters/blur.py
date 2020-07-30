import cv2
import numpy


class BlurFilter:
    def __init__(self, capture_device=cv2.VideoCapture(0)):
        self.capture_device = capture_device


    def make_1080p(self):
        self.capture_device.set(3, 1920)
        self.capture_device.set(4, 1080)

    @staticmethod
    def apply_blur(frame):
        blur = cv2.GaussianBlur(frame, (7, 7,), cv2.BORDER_DEFAULT)
        frame = cv2.cvtColor(blur, cv2.COLOR_BGRA2BGR)
        return frame

    def execute_filter(self):
        self.make_1080p()
        while True:

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            ret, frame = self.capture_device.read()
            blur = self.apply_blur(frame)

            cv2.imshow('blur', blur)

        self.capture_device.release()
        cv2.destroyAllWindows()
