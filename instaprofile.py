import requests
from bs4 import BeautifulSoup
username = "balapavan9"
url = 'https://www.instagram.com/{0}/'
r = requests.get(url.format(username ))
s = BeautifulSoup(r.text, 'html.parser')
u = s.find('meta', property='og: image')
# url = u.attrs['content']
with open(username +'.jpg','wb' ) as pic:
   b = requests.get(url).content
   pic.write(b)





# import webbrowser
# url = input( "Enter the post url:")
# download_url = "savefrom.net/"+url
# webbrowser.open(download_url)
