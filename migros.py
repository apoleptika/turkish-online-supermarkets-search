
#### This program scrapes naukri.com's page and gives our result as a 
#### list of all the job_profiles which are currently present there. 
# https://scrapingant.com/blog/scrape-dynamic-website-with-python

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


#url of the page we want to scrape
# url = "https://www.naukri.com/top-jobs-by-designations# desigtop600"
# url = "https://www.migros.com.tr/arama?q=dana%20k%C4%B1yma"  
# utf = "https://www.migros.com.tr/arama?q=ekmek"


def migros_get_data(search_product):
    print("")
    # utf8_search_words = "gazoz"
    utf8_search_words = search_product
    ascii_search_words = urllib.parse.quote(utf8_search_words)
    url ="https://www.migros.com.tr/arama?q=" + ascii_search_words
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
    
    # all_divs = soup.find('div', {'class' : 'mdc-layout-grid__inner product-cards list'})
    # all_divs = soup.find('div', {'class' : 'content mdc-layout-grid__inner'})
    all_divs = soup.find('div', {'class' : 'products'})
    #print(all_divs)
    products = all_divs.find_all('a', {'class' : 'mat-caption text-color-black product-name'})
    prices = all_divs.find_all('span', {'class' : 'amount'})

    """
    try:
        pages_all = soup.find('div', {'class' : 'page-row ng-star-inserted'})
        pages = pages_all.find_all('span', {'class' : 'mdc-button__label'})
        count = 0
        for item in pages :
            if item.text:
                print("Migros search pages : " + item.text)
                count=count+1
    except Exception as e :
        print('Migros multi page error. Try Except error meesage: ' , e)    
    """
    
    # printing top ten job profiles
    list1=[]
    list2=[]
    data_frame1 = pd.DataFrame()
    data_frame2 = pd.DataFrame()

    count = 0
    for item in products :
        # print(item.text)
        count=count+1
        list1.append([count, "Migros", item.text])

    count=0  
    for item in prices :
        # print(item.text)
        count=count+1
        list2.append([count, item.text])

    data_frame1 = pd.DataFrame(list1)
    data_frame1.columns = ['No', "Market", 'Product']
    data_frame2 = pd.DataFrame(list2)
    data_frame2.columns = ['No', 'Price']
    all_data_frame = pd.merge(data_frame1,data_frame2, how="left", on=["No"])

    # print(tabulate(all_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))
    # closing the webdriver
    driver.close() 
    return all_data_frame
    
# migros_data_frame = migros_get_data("ekmek")
# print(tabulate(migros_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))

