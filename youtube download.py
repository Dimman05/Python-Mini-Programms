from pytube import YouTube

url = input('Enter a url:')
video = YouTube(url)

print(video.title)

for stream in video.streams:
    if "video" in str(stream) and 'mp4' in str(stream):
        print(stream)

stream = video.streams.first()
print("Downloading...")
stream.download()
print('Done')


