import pytube

video_link: str = input("Input Your Link: ")

#video_link = "https://www.youtube.com/watch?v=a1wvgLkyVfQ"
yt = pytube.YouTube(video_link)
videos = yt.streams.first()
videos.download('I:\\Opening Video')