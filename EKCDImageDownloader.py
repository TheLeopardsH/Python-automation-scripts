#!usr/bin/python3

#script for downloading all comic images from XKCD.com
import requests
import bs4,os
from pathlib import Path
pathf =Path.cwd()
Website = 'https://xkcd.com'  #url
if not os.path.exists(Path(pathf/'xkcd')):
    os.makedirs(Path(pathf/'xkcd'))
else:
    pass
# or os.makedirs('xkcd',exist_ok=True)
while not Website.endswith('#'):#Last comic ends with https://xkcd.com/#
    #print('Download comic image from page %s'%Website)
    DownloadWebsite = requests.get(Website)
    try:
        DownloadWebsite.raise_for_status()
    except  Exception as exc:
        print('something goes wrong %s' % exc)
    bs = bs4.BeautifulSoup(DownloadWebsite.text,'html.parser')
    ComicElement = bs.select('#comic img')
    if ComicElement == []:
        print('Image not Found')
    else:
        DownloadImageUrl = 'https:'+ComicElement[0].get('src')
        print('Download comic image from page %s'%DownloadImageUrl)
        res = requests.get(DownloadImageUrl)
        try:
            res.raise_for_status()
        except  Exception as exc:
            print('something goes wrong %s' % exc)
        ImageDownload =open(os.path.join('xkcd',os.path.basename(DownloadImageUrl)),'wb')
        for chunk in res.iter_content(10000):
            ImageDownload.write(chunk)
        ImageDownload.close()
    PrevLink = bs.select('a[rel="prev"]')[0]
    Website = 'https://xkcd.com'+PrevLink.get('href')

print('Done Download all images')
