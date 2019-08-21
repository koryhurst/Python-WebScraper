
# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#Beautiful Soup Functions
def GetLinkList(UrlToSearch, SearchTerm): #or searchtermSSSS at some point
  # Connect to the URL
  response = requests.get(UrlToSearch)
  #print(response.text)
  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(response.text, "html.parser")
  linklist = []
  # To download the whole data set, let's do a for loop through all a tags
  #print(soup.findAll('a'))
  for i in range(36, len(soup.findAll('a')),1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    if SearchTerm in link:
      linklist.append(link)
  return linklist

def GetSoup(UrlToGet):
  response = requests.get(UrlToGet)
  #print(response.text)
  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(response.text, "html.parser")
  return soup
  
def SearchSoup(UrlToSearch, SearchTerm): #or searchtermSSSS at some point
  # Connect to the URL
  response = requests.get(UrlToSearch)
  #print(response.text)
  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(response.text, "html.parser")
  return soup.findAll(SearchTerm)

def ShowPrettySoup(UrlToShow):
  response = requests.get(UrlToShow)
  #print(response.text)
  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(response.text, "html.parser")
  print(soup.prettify)

def ShowLinks(UrlToShow):
  response = requests.get(UrlToShow)
  #print(response.text)
  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(response.text, "html.parser")
  #print(soup.find_all('a'))
  for link in soup.find_all('a'):
    print(link.get('href'))

#List Functions
def RemoveDupesFromList(ListToClean):
  return list(dict.fromkeys(ListToClean))



LinksToIndexPages = GetLinkList('https://members.nanaimochamber.bc.ca/list/','searchalpha')
for IndexPage in LinksToIndexPages:
  #print(IndexPage)
  LinksToBusinesPages = GetLinkList(IndexPage,'t/member/')  
  for BusinessLink in RemoveDupesFromList(LinksToBusinesPages):
    #print(BusinessLink)
    BusinessSoup = GetSoup(BusinessLink)
    #ShowPrettySoup(BusinessLink)
    print(BusinessSoup.find_all("h1", class_="gz-pagetitle"))
    print(BusinessSoup.find_all("span", class_="gz-cat"))
    print(BusinessSoup.find_all("span", class_="gz-street-address"))
    print(BusinessSoup.find_all("span", class_="gz-address-city"))
    print(BusinessSoup.find_all(itemprop="addressRegion"))
    print(BusinessSoup.find_all(itemprop="postalCode"))
    print(BusinessSoup.find_all(itemprop="telephone"))
    print(BusinessSoup.find_all(itemprop="faxNumber"))
    BusinessUrlMessy = str(BusinessSoup.find_all(itemprop="url", class_="card-link")[0])
    #print(type(BusinessUrlMessy))
    print(BusinessUrlMessy[27:BusinessUrlMessy.find("itemprop",0)-1])
    #print(BusinessUrlMessy[0])