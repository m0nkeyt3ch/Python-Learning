#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as BS
import sys

main_url = "https://tw.voicetube.com/channel/translated"

def getMaxPageNum(body):
    page_navi = body.find("div", {"class": "pagination"})
    last_page_num = page_navi.find_all("li")[-1].find("a")["data-ci-pagination-page"]
    return last_page_num

def getPageVids(pgid):
    pgid = str(pgid)
    url = main_url + "/" + pgid
    r = requests.get(url)
    body = BS(r.text, "html.parser").body
    vids = set()
    vlist = body.find("ul", {"class": "thumbnails vt-video-list"})
    for video in vlist.find_all("li"):
        #print(video.find("div", {"class": "thumbnail"})["data-video-id"])
        vids.add(video.find("div", {"class": "thumbnail"})["data-video-id"])
    return vids

def getVideoCaption(vid):
    url = "https://tw.voicetube.com/videos/print/" + vid + "?eng_zh_tw=1"
    r = requests.get(url)
    body = BS(r.text, "html.parser").body
    return body.find("ol").get_text(separator = "\t")

if __name__ == '__main__':
    import argparse
    import os
    parser = argparse.ArgumentParser(description="Voicetube.com crawler",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-o", "--out-dir", help = "directory to store output caption files", default = "./captions")
    args = parser.parse_args()

    if not os.path.exists(args.out_dir):
        os.mkdir(args.out_dir)

    r = requests.get(main_url)
    body = BS(r.text, "html.parser").body
    for pid in range(int(getMaxPageNum(body))):
        for vid in getPageVids(pid):
            fvideo = args.out_dir + "/" + vid + ".txt"
            with open(fvideo, 'w') as fp:
                print("NOTICE: parsing video", vid, file = sys.stderr)
                fp.write(getVideoCaption(vid))
#print(r.text)
