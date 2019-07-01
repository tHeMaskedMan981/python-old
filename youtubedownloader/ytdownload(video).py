import pafy, pyperclip


vd=pafy.new("https://www.youtube.com/watch?v=RUqC4MG7FWk")

best=vd.getbest(preftype="mp4")
best.download()
