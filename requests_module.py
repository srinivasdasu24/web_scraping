"""
Explains usage of "requests" module and how to get data from web using it
requests.readthedocs.org -- requests module
It is good for downloading file, webpages when we have exact url
Figuring out url and other things will be difficult with requests module
"""
import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

res.status_code # if it returns 200 then above command executed succesfully 

len(res.text)

print(res.text[:500])

res.raise_for_status()  # raises an exception if file is not downloaded properly otherwise won't

fileplay=open("data.txt","a")
for chunk in res.iter_content(10000):
  fileplay.write(chunk)
  
