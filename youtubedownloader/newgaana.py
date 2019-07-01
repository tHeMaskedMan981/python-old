import pafy


songStreams=song.audiostreams

for s in songStreams :
	if s.extension == 'mp4':
		gaana=s
		break

gaana.dowload()