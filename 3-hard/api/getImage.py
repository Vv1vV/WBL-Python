import requests
import datetime
import urllib.parse
import json

from pytube import YouTube


class NasaAPI:
    def __init__(self, hd, api_key, date=False):
        self.url = 'https://api.nasa.gov/planetary/apod?'
        self.hd = hd
        self.date = None
        self.api_key = api_key
        self.getDate(date)

    def getDate(self, date):
        curDate = datetime.datetime.now()
        self.date = curDate.strftime("%Y-%m-%d")
        if type(date) == int:
            curDate = self.date.split('-')
            newDate = datetime.datetime(
                int(curDate[0]), int(curDate[1]), int(curDate[2]))

            timedelta = datetime.timedelta(date)
            self.date = (newDate - timedelta).strftime("%Y-%m-%d")

    def getLink(self):
        options = {
            'api_key': self.api_key,
            'hd': self.hd,
            'date': self.date
        }

        return self.url + urllib.parse.urlencode(options)

    def getImage(self):
        link = self.getLink()
        linkContent = requests.get(link).content.decode()

        decodeContent = json.loads(str(linkContent))

        if self.hd:
            if 'hdurl' in decodeContent.keys():
                url = decodeContent["hdurl"]
            else:
                url = decodeContent["url"]
        else:
            url = decodeContent["url"]

        title = '-'.join(decodeContent["title"].split(' '))

        if decodeContent['media_type'] == 'video':
            player = urllib.parse.urlsplit(url).netloc.split('.')[1]

            if player == 'youtube':
                YouTube(url).streams.filter(file_extension="mp4").order_by(
                    'resolution')[-1].download("./Videos/")
            elif player == "vimeo":
                return
            else:
                return
        else:
            img_data = requests.get(url).content
            with open("./Images/" + title + '.jpg', 'wb') as handler:
                handler.write(img_data)
