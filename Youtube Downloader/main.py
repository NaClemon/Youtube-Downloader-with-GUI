# Youtube Downloader
# Copyright NaClemon

import os
import sys

import googleapiclient.discovery
import googleapiclient.errors

import PyQt5.QtWidgets as Qt

import youtube_dl as yd

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

class Window(Qt.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.searchArea()
        self.videoQuality()

        hbox = Qt.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(self.sbox)
        hbox.addWidget(self.video_cb)
        hbox.addStretch(1)

        self.setLayout(hbox)

        self.setWindowTitle("Test Window")
        self.resize(1200, 720)
        self.setWindowToCenter()
        self.show()

    def setWindowToCenter(self):
        window_inform = self.frameGeometry()
        center_monitor = Qt.QDesktopWidget().availableGeometry().center()
        window_inform.moveCenter(center_monitor)
        self.move(window_inform.topLeft())

    def searchArea(self):
        self.search_label = Qt.QLabel("검색어: ", self)
        self.search_line = Qt.QLineEdit(self)

        self.search_btn = Qt.QPushButton("Search", self)
        self.search_btn.setCheckable(True)

        self.sbox = Qt.QHBoxLayout()
        self.sbox.addStretch(1)
        self.sbox.addWidget(self.search_label)
        self.sbox.addWidget(self.search_line)
        self.sbox.addWidget(self.search_btn)
        self.sbox.addStretch(8)

    def videoQuality(self):
        self.video_cb = Qt.QComboBox(self)
        self.video_cb.addItem("chk", 100)

    def audioQuality(self):
        self.audio_cb = Qt.QComboBox(self)
        self.audio_cb.addItem("chk", 100)

class Downloader:
    def __init__(self):
        self.options = {}

    def downloadVid(self, url):
        self.ydl = yd.YoutubeDL(self.options)
        for inform, value in self.ydl.extract_info(url, False).items():
            print(inform + ": " + str(value))


# def main():
#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
#
#     api_service_name = "youtube"
#     api_version = "v3"
#     api_key = ""
#
#     # Get credentials and create an API client
#     youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, developerKey=api_key)
#
#     request = youtube.search().list(
#         part="snippet",
#         q="요루시카"
#     )
#     response = request.execute()
#
#     print(response)

if __name__ == "__main__":
    yt_downloader = Downloader()
    yt_downloader.downloadVid("https://www.youtube.com/watch?v=CS4f3jawFxY")