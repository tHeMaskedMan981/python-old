import webbrowser , os, requests

res=requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

downlfile=open(' romeo&juliet.txt','wb')
for chunk in res.iter_content(10000):
    downlfile.write(chunk)

print chunk    

downlfile.close()    
