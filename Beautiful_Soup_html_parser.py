"""

Explains usage of beautiful soup and how to parse the html content

"""

# Getting price from amazon
import bs4
import requests

def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#newOfferAccordionRow .header-price')
    return elems[0].text.strip()


price = getAmazonPrice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=tmm_pap_swatch_0?_encoding=UTF8&amp;qid=&amp;sr=')
print('The price is ' + price)



import bs4
import requests

# add headers so amazon will allow to get info, otherwise it will think you as a robot
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
res=requests.get("https://www.amazon.in/Automate-Boring-Stuff-Python-2nd/dp/1593279922",headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')

