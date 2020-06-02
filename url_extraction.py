from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"

response =requests.get(url)
print(response)

data = response.text

#print(data)

soup = BeautifulSoup(data,'html.parser')


# for extracting url links
#tags = soup.find_all('a')
#for tag in tags:
#    print(tag.get('href'))

# For extracting titles
titles = soup.find_all("a",{"class":"result-title"})

for title in titles:
    print(title.text)

# for extracting addresses

addresses = soup.find_all("span",{"class":"result-hood"})

for address in addresses:
    print(address.text)

# For extracting full job details

jobs = soup.find_all('p',{"class":"result-info"})

for job in jobs:
    title=job.find('a',{"class":"result-title"}).text
    location_tag=job.find('span',{"class":"result-hood"})
    location = location_tag.text if location_tag else "N/A"
    date = job.find('time',{"class":"result-date"}).text
    link=job.find('a',{"class":"result-title"}).get('href')
    job_response = requests.get(link)
    job_data = job_response.text
    job_soup= BeautifulSoup(job_data,"html.parser")
    job_description = job_soup.find('section',{'id':'postingbody'}).text
    job_attributes_tag = job_soup.find('p',{'class':'attrgroup'})
    job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
    print('Job title :', title, '\n Location : ', location ,'\nDate : ', date,'\nLink : ', link, '\nJob Attributes : ',job_attributes ,'\nJob Description : ',job_description, '\n--------')
