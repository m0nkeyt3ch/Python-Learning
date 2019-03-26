import pytube

#video_link: str = input("Input Your Link: ")

video_link = "https://www.youtube.com/watch?v=SMk2m5uasdM"
yt = pytube.YouTube(video_link)
videos = yt.streams.first()
videos.download ('C://desktop')