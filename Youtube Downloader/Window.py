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
    window_title = "Youtube Downloader"
    width = 800
    height = 600

    def __init__(self):
        super().__init__()
        self.yt_downloader = Downloader.Downloader()
        # Search
        self.search_label = Qt.QLabel("검색어: ", self)
        self.search_line = Qt.QLineEdit(self)
        self.search_btn = Qt.QPushButton("Search", self)
        self.video_ck = Qt.QCheckBox("Best Video", self)
        self.audio_ck = Qt.QCheckBox("Best Audio", self)
        self.search_box = Qt.QHBoxLayout()
        # Download Option
        # self.video_cb = Qt.QComboBox()
        # self.audio_cb = Qt.QComboBox()
        # Result
        self.scrollBox = Qt.QScrollArea()
        self.download_btns = []
        self.initUI()

    def initUI(self):
        self.scrollBox.setFixedHeight(400)
        self.searchArea()
        self.makeLayout()
        self.createWindow()

    def createWindow(self):
        self.setWindowTitle(self.window_title)
        self.resize(self.width, self.height)
        self.setWindowToCenter()
        self.show()

    def setWindowToCenter(self):
        window_inform = self.frameGeometry()
        center_monitor = Qt.QDesktopWidget().availableGeometry().center()
        window_inform.moveCenter(center_monitor)
        self.move(window_inform.topLeft())

    def makeLayout(self):
        vbox = Qt.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(self.search_box)
        vbox.addWidget(self.scrollBox)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def searchArea(self):
        self.search_btn.pressed.connect(lambda : self.setResultArea(self.search_line.text()))

        self.search_box.addStretch(1)
        self.search_box.addWidget(self.search_label)
        self.search_box.addWidget(self.search_line)
        self.search_box.addWidget(self.search_btn)
        self.search_box.addWidget(self.video_ck)
        self.search_box.addWidget(self.audio_ck)
        self.search_box.addStretch(1)

    def setResultArea(self, url):
        vid_list = self.getVidsList(url)
        # List Area
        list_box = Qt.QVBoxLayout()

        for vids in vid_list:
            # Video Area
            vid_box = Qt.QHBoxLayout()
            vid_box.addStretch(1)
            # Video's Detail Area
            detail_box = Qt.QVBoxLayout()
            detail_box.setContentsMargins(35, 0, 0, 0)
            download_btn = Qt.QPushButton("Download", self)
            for vid_key, vid_val in vids.items():
                lb = Qt.QLabel()
                if vid_key == 'thumbnails':
                    imageFromWeb = urllib.request.urlopen(vid_val[0]['url']).read()
                    thumbnail = Qg.QPixmap()
                    thumbnail.loadFromData(imageFromWeb)
                    lb.setPixmap(thumbnail)
                    vid_box.addWidget(lb)
                elif vid_key == 'webpage_url':
                    lb.setText(vid_key + ": <a href='" + str(vid_val) + "'>check</a>")
                    lb.setOpenExternalLinks(True)
                    download_btn.pressed.connect(lambda : self.yt_downloader.downloadVid(str(vid_val)))
                    self.download_btns.append(download_btn)
                    detail_box.addWidget(lb)
                else:
                    lb.setText(vid_key + ": " + str(vid_val))
                    detail_box.addWidget(lb)
            vid_box.addLayout(detail_box)
            vid_box.addWidget(download_btn)
            vid_box.addStretch(1)
            list_box.addLayout(vid_box)

        if len(vid_list) == 0:
            lb = Qt.QLabel("There is no video.")
            list_box.addWidget(lb)

        scroll_widget = Qt.QWidget()
        scroll_widget.setLayout(list_box)
        self.scrollBox.setWidget(scroll_widget)

    def getVidsList(self, url):
        vid_list = []
        log = open("Error_Logs.txt", 'w', encoding='UTF8')
        try:
            vid = {}
            vid_informs = self.yt_downloader.downloadVid(url)
            for key, val in vid_informs.items():
                if key in vid_inform:
                    vid[key] = val
            vid_list.append(vid)
        except:
            print("There is Error in " + url, file=log)
        log.close()
        return vid_list

    def videoQuality(self, vd_qual):
        self.video_cb.addItem("bestvideo", 100)
        for qual in vd_qual:
            self.video_cb.addItem(qual, int(qual[0:-1]))

    def audioQuality(self, ad_qual):
        self.audio_cb.addItem("bestaudio", 100)
        for qual in ad_qual:
            self.audio_cb.addItem(qual, int(qual[0:-1]))