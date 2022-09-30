
#### This program scrapes naukri.com's page and gives our result as a 
#### list of all the job_profiles which are currently present there. 
# https://scrapingant.com/blog/scrape-dynamic-website-with-python
#   
#https://stackoverflow.com/questions/67501093/passthrough-is-not-supported-gl-is-disabled
# I had the same problem with selenium and chromedriver. For me the solution was to activate WebGL in Chrome browser. I did the following
# chrome://settings -> Click Advanced at the bottom -> Check the Use hardware acceleration when available box

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# if you need install package Tabulate,  pip install tabulate
from tabulate import tabulate
# if you need install package Pandas,  pip install pandas
import pandas as pd
import urllib.parse


# url of the page we want to scrape
# url = "https://www.sokmarket.com.tr/arama/ekmek"
# url = "https://www.sokmarket.com.tr/arama/dana%20k%C4%B1yma"


def sokmarket_get_data(search_product):
    print("")
    # utf8_search_words = "domates salça"
    utf8_search_words = search_product
    ascii_search_words = urllib.parse.quote(utf8_search_words)
    url ="https://www.sokmarket.com.tr/arama/" + ascii_search_words
    print(url)

    # initiating the webdriver. Parameter includes the path of the webdriver.
    # driver = webdriver.Chrome('./chromedriver') 
    # driver.get(url) 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # this is just to ensure that the page is loaded
    time.sleep(5) 
    
    html = driver.page_source
    
    # this renders the JS code and stores all
    # of the information in static HTML code.
    
    # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")

    # all_divs = soup.find('div', {'id' : 'nameSearch'})
    # job_profiles = all_divs.find_all('a')

    # all_divs = soup.find('div', {'class' : 'results-container'})
    all_divs = soup.find('main', {'class' : 'listing-results'})
    products = all_divs.find_all('strong', {'class' : 'content-title'})
    # prices = all_divs.find('ul',{'class' : 'results-list'} ).find('div', {'class' : 'pricetag content-prices'}).find('span')
    # prices = all_divs.find_all('ul', {'class' : 'results-list'}).find('li', {'class' : 'list-item'}).find('div', {'class' : 'pricetag content-prices'}).find('span')
    # prices = all_divs.find('ul', {'class' : 'results-list'}).find('li', {'class' : 'list-item'}).find('span')
    prices = all_divs.find_all(['productbox-content','pricetag content-prices', 'span'])

    list1=[]
    list2=[]
    data_frame1 = pd.DataFrame()
    data_frame2 = pd.DataFrame()
    
    count = 0
    for item in products :
        # print(item.text)
        count=count+1
        list1.append([count, "Şok Market", item.text])

    count=0  
    for item in prices :
        if not item.text == "0":
            count=count+1
            # print(count, " price : " , item.text) 
            list2.append([count, item.text])

    data_frame1 = pd.DataFrame(list1)
    data_frame1.columns = ['No', "Market", 'Product']
    data_frame2 = pd.DataFrame(list2)
    data_frame2.columns = ['No', 'Price']
    all_data_frame = pd.merge(data_frame1,data_frame2, how="left", on=["No"])

    # print(tabulate(all_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))
    driver.close() # closing the webdriver
    return all_data_frame


# sokmarket_data_frame = sokmarket_get_data("ekmek")
# print(tabulate(sokmarket_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))


