import youtube_dl as yd

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
        print("check")
        inform = self.ydl.extract_info(url, False)
        f = open("result.txt", 'w', encoding='UTF8')
        for a, b in inform.items():
            print(a + ": " + str(b), file=f)
            print("----------------------", file=f)
        f.close()
        return inform