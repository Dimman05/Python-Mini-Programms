# pip install pytube
from pytube import YouTube

# We create a empty list
video_list = []


print('Enter the URLs (Terminate with STOP)')

# Mainloop
while True:
    url = input('>>')
    if url == 'STOP':
        break
    video_list.append(url)

for video in video_list:
    v = YouTube(video)
    stream = v.streams.get_by_itag(22)
    print('Downloading' + video.title())
    stream.download()
    print('Done')