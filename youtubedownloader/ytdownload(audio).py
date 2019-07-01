import pafy

video=pafy.new("https://www.youtube.com/watch?v=AJtDXIazrMo")

audiostreams=video.audiostreams
flag=0
for a in audiostreams :
	print(a.extension)
    if (a.extension=='mp3') :
        a.download()
        flag=1

if flag==0 :
	bestaudio=video.getbestaudio()
	bestaudio.download()
