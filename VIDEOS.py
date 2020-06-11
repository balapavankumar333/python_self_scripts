import pytube
link = "https://www.youtube.com/watch?v=AImD1AjhgnQ"  # paste the link you want to download from youtube
yt =pytube.YouTube(link)
yt.streams.first().download()
print("Completed",link)
