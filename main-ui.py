import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('YouTube Music Downloader')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(100, 100, 400, 200)

        self.setStyleSheet("background-color: #212529; color: #dee2e6;")

        self.url_label = QLabel('Video URL:')
        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; padding: 5px; border-radius: 5px; }")

        self.name_label = QLabel('File Name:')
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; padding: 5px; border-radius: 5px; }")

        self.download_button = QPushButton('Download and Process')
        self.download_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px 24px; border-radius: 5px; }"
                                           "QPushButton:hover { background-color: #45a049; }")
        self.download_button.clicked.connect(self.download_and_process)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.url_label)
        main_layout.addWidget(self.url_input)
        main_layout.addWidget(self.name_label)
        main_layout.addWidget(self.name_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.download_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        font = QFont()
        font.setPointSize(10)
        self.setFont(font)

    def download_and_process(self):
        url = self.url_input.text()
        name = self.name_input.text()

        if not url or not name:
            QMessageBox.critical(self, "Error", "Please enter URL and file name!")
            return

        control = QMessageBox.question(self, "Confirmation", "Are you sure you want to proceed?", 
                                       QMessageBox.Yes | QMessageBox.No)

        if control == QMessageBox.Yes:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution().download()

            videoclip = VideoFileClip(video)
            audioclip = videoclip.audio 

            audioclip.write_audiofile(name + ".wav")

            videoclip.close()
            audioclip.close()
            os.remove(video)

            QMessageBox.information(self, "Success", "Video processed successfully!")
        else:
            QMessageBox.information(self, "Info", "Process aborted.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())