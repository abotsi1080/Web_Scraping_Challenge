# Importing the needed Dependencies
import requests
import pymongo
import pandas as pd
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

def savetofile(contents):
    file = open('_temporary.txt',"w",encoding="utf-8")
    file.write(contents)
    file.close()

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser=init_browser()
    mars_data={}
    ### NASA Mars News

    # Defining the url of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')

    # Retrieving the latest news title
    news_title=soup.find_all('div', class_='content_title')[0].text
    # Retrieving the latest news paragraph
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text
    
    ### JPL Mars Space Images - Featured Image
    # Obtaining the url for the featured space image site
    featured_url="https://redplanetscience.com/"
    featured_image_url="https://mars.nasa.gov/system/news_items/list_view_images/8567_PIA23517-320x240.jpg"
    #browser.visit(featured_image_url)

    base_url = "https://spaceimages-mars.com/"
    browser.visit(base_url)
    time.sleep(3)

    # Defining HTML object
    html = browser.html
    # Parsing HTML
    soup = bs(html,"html.parser")
    # Retrieve image url
    image_url = soup.find("img", class_ = "headerimage fade-in")["src"]
    image_url

    featured_image_url = base_url + image_url
    print(featured_image_url)

    ### Mars Fact

    # Scrape Mars facts from galaxyfacts website
    url='https://galaxyfacts-mars.com/'
    html_tables = pd.read_html(url)
    
    mars_fact = html_tables[0]
    mars_fact=mars_fact.rename(columns={0:"Profile",1:"Value"},errors="raise")
    mars_fact.set_index("Profile",inplace=True)
    mars_fact
    
    mars_fact_table=mars_fact.to_html()
    mars_fact_table.replace('\n','')
    print(mars_fact_table)

    ### Mars Hemispheres

    # Navigate to the url for scraping
    base_url='https://marshemispheres.com/'
    browser.visit(base_url)
    time.sleep(3)

    #Container to hold  our loop iterations
    hemisphere_image_urls  = []

    #Iterate through the 4 different links to get the images needed
    for item in range(4):
        html = browser.html
        soup = bs(html, "html.parser")
        
        title = soup.find_all("h3")[item].get_text()
        browser.find_by_tag("h3")[item].click()
        
        html = browser.html
        soup = bs(html, "html.parser")
        
        hemisphere_url = soup.find("img", class_="wide-image")["src"]
        hemisphere_image_urls.append({
            "title":title,
            "img_url": base_url+hemisphere_url
        })
    
        browser.back()
    hemisphere_image_urls 

    mars_data = {}
    # Create dictionary for all info scraped from sources above
    mars_data = {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "fact_table":mars_fact_table,
        "hemisphere_images":hemisphere_image_urls
    }
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data