import os

import youtube_dl as yd

import googleapiclient.discovery
import googleapiclient.errors

class Downloader:
    def __init__(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        self.options = {
            'format': 'best/best',
            'outtmpl': '',
        }
        self.request_param = {
            'part': 'snippet',
            'maxResults': 10,
            'q': '',
            'type': 'video'
        }
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.api_key = ""

    def setBuildEnv(self, api_key):
        try:
            self.youtube = googleapiclient.discovery.build(
                self.api_service_name, self.api_version, developerKey=self.api_key)
            return True
        except:
            return False

    def getQualityInfo(self, url):
        vd_infos = []
        ad_infos = []

    def searchVid(self, search_word):
        return []

    def downloadVid(self, url, is_download=False, path=''):
        self.options['outtmpl'] = path + '/YoutubeVideos/%(title)s.%(ext)s'
        self.ydl = yd.YoutubeDL(self.options)
        inform = self.ydl.extract_info(url, is_download)
        f = open("result.txt", 'w', encoding='UTF8')
        for a, b in inform.items():
            print(a + ": " + str(b), file=f)
            print("----------------------", file=f)
        f.close()
        return inform