import PyQt5.QtWidgets as Qt
import PyQt5.QtGui as Qg
import urllib.request
import Downloader

vid_inform = [
    "uploader",
    "title",
    "thumbnails",
    "webpage_url",
]

class Window(Qt.QWidget):
    videoOptions = []
    audioOptions = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Search Area
        self.searchArea()
        # 스크롤 에리어
        self.scrollBox = Qt.QScrollArea()
        self.scrollBox.setFixedHeight(400)

        vbox = Qt.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(self.sbox)
        vbox.addWidget(self.scrollBox)
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

        self.video_ck = Qt.QCheckBox("Best Video", self)
        self.audio_ck = Qt.QCheckBox("Best Audio", self)

        self.sbox = Qt.QHBoxLayout()
        self.sbox.addStretch(1)
        self.sbox.addWidget(self.search_label)
        self.sbox.addWidget(self.search_line)
        self.sbox.addWidget(self.search_btn)
        self.sbox.addWidget(self.video_ck)
        self.sbox.addWidget(self.audio_ck)
        self.sbox.addStretch(1)

    def setVidInform(self, url):
        # Video List
        vidList = Qt.QVBoxLayout()
        # Video Inform
        vid_box = Qt.QHBoxLayout()
        vid_box.addStretch(1)
        # Video Detail
        detail_box = Qt.QVBoxLayout()
        detail_box.setContentsMargins(35, 0, 0, 0)
        try:
            yt_downloader = Downloader.Downloader()
            informs = yt_downloader.downloadVid(url)
            for key, val in informs.items():
                if key in vid_inform:
                    if key == 'thumbnails':
                        lb = Qt.QLabel()
                        imageFromWeb = urllib.request.urlopen(val[0]['url']).read()
                        qpix = Qg.QPixmap()
                        qpix.loadFromData(imageFromWeb)
                        lb.setPixmap(qpix)
                        vid_box.addWidget(lb)
                    elif key == 'webpage_url':
                        lb = Qt.QLabel(key + ": <a href='" + str(val) + "'>check</a>")
                        lb.setOpenExternalLinks(True)
                        detail_box.addWidget(lb)
                    else:
                        lb = Qt.QLabel(key + ": " + str(val))
                        detail_box.addWidget(lb)
        except:
            lb = Qt.QLabel("There is no video.")
            detail_box.addWidget(lb)
        vid_box.addLayout(detail_box)
        vid_box.addStretch(1)
        vidList.addLayout(vid_box)
        widget = Qt.QWidget()
        widget.setLayout(vidList)
        self.scrollBox.setWidget(widget)

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