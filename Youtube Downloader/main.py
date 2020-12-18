# Youtube Downloader
# Copyright NaClemon

import os
import sys

import googleapiclient.discovery
import googleapiclient.errors

import PyQt5.QtWidgets as Qt

import youtube_dl as yd

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

vid_inform = {
    "uploader": '',
    "title": '',
    "thumbnails": [],
    "webpage_url": '',
    "formats": []
}
vid_format = {
    "format_id": 0,
    "ext": '',
    "width": 0,
    "height": 0,
    "format": '',
}

class Window(Qt.QWidget):
    videoOptions = []
    audioOptions = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.searchArea()
        self.tb = Qt.QTextBrowser()

        video_ck = Qt.QCheckBox("Best Video", self)
        audio_ck = Qt.QCheckBox("Best Audio", self)

        hbox = Qt.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(self.sbox)
        hbox.addWidget(video_ck)
        hbox.addWidget(audio_ck)
        hbox.addStretch(1)

        vbox = Qt.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.tb)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle("Test Window")
        self.resize(800, 600)
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
        self.search_btn.pressed.connect(lambda : self.setVidInform(self.search_line.text()))

        self.sbox = Qt.QHBoxLayout()
        self.sbox.addStretch(1)
        self.sbox.addWidget(self.search_label)
        self.sbox.addWidget(self.search_line)
        self.sbox.addWidget(self.search_btn)
        self.sbox.addStretch(8)

    def setVidInform(self, url):
        self.tb.clear()
        try:
            yt_downloader = Downloader()
            informs = yt_downloader.downloadVid(url)
            for key, val in informs.items():
                self.tb.append(key + ": " + str(val))
                self.tb.append("---------------------------------")
        except:
            self.tb.append("There is no video.")

    def videoQuality(self, vd_qual):
        self.video_cb = Qt.QComboBox(self)
        self.video_cb.addItem("bestvideo", 100)
        for qual in vd_qual:
            self.video_cb.addItem(qual, int(qual[0:-1]))

    def audioQuality(self, ad_qual):
        self.audio_cb = Qt.QComboBox(self)
        self.audio_cb.addItem("bestaudio", 100)
        for qual in ad_qual:
            self.audio_cb.addItem(qual, int(qual[0:-1]))

class Downloader:
    def __init__(self):
        self.options = {
            'format': 'best/best',
        }

    def getQualityInfo(self, url):
        vd_infos = []
        ad_infos = []

    def downloadVid(self, url):
        self.ydl = yd.YoutubeDL(self.options)
        inform = self.ydl.extract_info(url, False)
        f = open("result.txt", 'w', encoding='UTF8')
        for a, b in inform.items():
            print(a + ": " + str(b), file=f)
            print("----------------------", file=f)
        f.close()
        return inform


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
    app = Qt.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())