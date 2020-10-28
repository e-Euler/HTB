import requests
import hashlib
from bs4 import BeautifulSoup

sesh = requests.Session()

url= ""    


page = sesh.get(url)
print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
code = soup.find("h3").text.strip()
print("Plain: "+code)
hash = hashlib.md5(str(code)).hexdigest()
print("md5: "+hash)
data=dict(hash=hash)
page_post = sesh.post(url=url, data=data)
print 
print(page_post.text)
