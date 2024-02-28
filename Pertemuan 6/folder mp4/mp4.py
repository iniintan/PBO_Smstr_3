import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer

class VideoPlayerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.video_path = None
        self.video_capture = None

        self.lbl_video = QLabel(self)
        self.btn_open = QPushButton('Open Video', self)
        self.btn_play_pause = QPushButton('Play', self)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_video)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_play_pause)

        self.setLayout(layout)

        self.btn_open.clicked.connect(self.open_video)
        self.btn_play_pause.clicked.connect(self.play_pause_video)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Video Player')
        self.show()

    def open_video(self):
        file_dialog = QFileDialog()
        self.video_path, _ = file_dialog.getOpenFileName(self, 'Open Video File', '', 'Video Files (*.mp4 *.avi *.mkv)')
        if self.video_path:
            self.video_capture = cv2.VideoCapture(self.video_path)
            self.play_video()

    def play_pause_video(self):
        if self.video_capture.isOpened():
            if self.timer.isActive():
                self.timer.stop()
                self.btn_play_pause.setText('Play')
            else:
                self.timer.start(33)  # 30 fps
                self.btn_play_pause.setText('Pause')

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.lbl_video.setPixmap(pixmap)

    def play_video(self):
        self.btn_play_pause.setText('Pause')
        self.timer.start(33)  # 30 fps

    def closeEvent(self, event):
        if self.video_capture is not None:
            self.video_capture.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player_app = VideoPlayerApp()
    sys.exit(app.exec_())