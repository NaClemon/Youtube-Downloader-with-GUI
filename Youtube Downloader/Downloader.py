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

    def setBuildEnv(self, api_key):
        try:
            self.youtube = googleapiclient.discovery.build(
                self.api_service_name, self.api_version, developerKey=api_key)
            return True
        except:
            return False

    def getQualityInfo(self, url):
        vd_infos = []
        ad_infos = []

    def getVidList(self, search_word):
        vid_list = []
        self.request_param['q'] = search_word
        additional_url = 'https://www.youtube.com/watch?v='
        request = self.youtube.search().list(
            part=self.request_param['part'],
            maxResults=self.request_param['maxResults'],
            q=self.request_param['q'],
            type=self.request_param['type']
        )
        vids = request.execute()
        for vid_inform in vids['items']:
            vid_list.append(additional_url + vid_inform['id']['videoId'])
        return vid_list

    def downloadVid(self, url, is_download=False, path=''):
        if path == '':
            path += './YoutubeVideos'
        self.options['outtmpl'] = path + '/%(title)s.%(ext)s'
        self.ydl = yd.YoutubeDL(self.options)
        inform = self.ydl.extract_info(url, is_download)
        return inform