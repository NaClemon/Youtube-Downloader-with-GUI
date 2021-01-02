import PyQt5.QtWidgets as Qt

class HelpWindow(Qt.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("도움말")
        self.resize(500, 300)
        self.helpMainText()
        layout = Qt.QVBoxLayout()
        self.label = Qt.QLabel(self.str)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def helpMainText(self):
        self.str = "<h1>사용 방법</h1>" \
                   "<h3>Api 적용</h3>" \
                   "<p>1. 구글 클라우드 플랫폼에 접속<br>" \
                   "2. 로그인 후 Youtube Data API v3를 발급<br>" \
                   "3. 발급 받은 키를 적용</p>" \
                   "<h3>저장 경로</h3>" \
                   "<p>저장 경로를 설정하지 않아도 됩니다.<br>" \
                   "설정하지 않을 경우 실행 파일이 있는 곳에 저장됩니다.<br>" \
                   "기본적으로 YoutubeVideos 폴더에 동영상이 저장됩니다.</p>" \
                   "<h3>검색 방법</h3>" \
                   "<p>Api를 설정하지 않으면 주소 지정 검색만 사용이 가능합니다.<br>" \
                   "일반 검색은 유튜브 검색과 같은 방법입니다.<br>" \
                   "오류가 일어나는 동영상 제외 총 10개의 동영상 목록을 보여줍니다.</p>"

class MenuWindow(Qt.QWidget):
    def __init__(self):
        super().__init__()
        layout = Qt.QVBoxLayout()
        self.label = Qt.QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)