from pytube import YouTube
yt= YouTube('https://www.youtube.com/watch?v=CGyEd0aKWZE')

print(yt.get_vedios())

video=yt.get('mp4','720p')

#video.download('C:\Users\akash\Desktop')
