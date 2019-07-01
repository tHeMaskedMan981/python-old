import webbrowser, sys, pyperclip

if len(sys.argv)>1 :
        adress=' '.join(sys.argv[1:])
else :
                        
        adress=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)                        
