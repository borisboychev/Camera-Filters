import cv2


class BlackAndWhite:
    def __init__(self, capture_device=cv2.VideoCapture(0)):
        self.capture_device = capture_device

    def make_1080p(self):
        self.capture_device.set(3, 1920)
        self.capture_device.set(4, 1080)

    def execute_filter(self):
        self.make_1080p()
        while True:

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            ret, frame = self.capture_device.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Black&White', gray)

        self.capture_device.release()
        cv2.destroyAllWindows()
