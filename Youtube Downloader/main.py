# Youtube Downloader
# Copyright NaClemon

import os
import sys

import Window

import googleapiclient.discovery
import googleapiclient.errors

import PyQt5.QtWidgets as Qt

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

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
    ex = Window.Window()
    sys.exit(app.exec_())