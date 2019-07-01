import pafy

song = pafy.new("https://www.youtube.com/watch?v=PT2_F-1esPk")
path="C:\Users\akash\Downloads"
gaana = song.getbestaudio()
gaana.download(path)
