from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
from matplotlib import pyplot as plt
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options    
from selenium.common.exceptions import NoSuchElementException
import time
import argparse

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  
driver = webdriver.Chrome(r'C:\Users\Shounak\SeleniumVitra\chromedriver.exe', chrome_options=options)

parser=argparse.ArgumentParser(description='Scraps the data and saves it in a CSV file')
parser.add_argument('language', metavar='language', type=str, help='Enter the language for which you want to scrap the Inshorts site ')
parser.add_argument('path', metavar='path', type=str, help='Enter the path where you want to save the CSV file ')
args= parser.parse_args()
language=args.language
path=args.path




driver.get('https://www.inshorts.com/'+language+'/read')
while True:
    try:
        loadMoreButton = driver.find_element(By.XPATH,"//*[@id='load-more-btn']")
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        print (e)
        break
print ("LOading all the pages.....Finished")
time.sleep(10)
df=pd.DataFrame()
dataf=pd.DataFrame()



elements=driver.find_elements(By.CLASS_NAME, "clickable")
headings=[]
for x in elements:
    headings.append(x.text)
headings=headings[ : -3]
headings=headings[ 2: ]
 

elements=driver.find_elements(By.CLASS_NAME, "news-card-content.news-right-box")
Content=[]
for x in elements:
    Content.append(x.text)


elements=driver.find_elements(By.CLASS_NAME, "news-card-author-time.news-card-author-time-in-title")
DateTime=[]
for x in elements:
    DateTime.append(x.text)


df['Heading']=headings
df['Content']=Content
df['DateTime']=DateTime
df.to_csv(r"" + path,index=False)
print("CSV File successfully created ! ")
