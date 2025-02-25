from threading import Thread
import cv2


class Multithreading:
    def __init__(self, src):
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.frame = None
        self.thread.start()

    def update(self):
        while True:
            _, self.frame = self.capture.read()

    def get_frame(self):
        return self.frame