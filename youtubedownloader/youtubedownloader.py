import pafy , pyperclip

adress=pyperclip.paste()
vd=pafy.new(adress)

best=vd.getbest(preftype="mp4")
best.download()
