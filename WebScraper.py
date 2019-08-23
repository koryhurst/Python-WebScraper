
# Import libraries
import requests
import urllib.request
import time
import csv

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
with open('NanaimoChamber.csv', mode='w') as writeFile:
  NanaimoChamberCSV = csv.writer(writeFile, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
  for IndexPage in LinksToIndexPages:
    #print(IndexPage)
    LinksToBusinesPages = GetLinkList(IndexPage,'t/member/')  
    for BusinessLink in RemoveDupesFromList(LinksToBusinesPages):
      #print(BusinessLink)
      BusinessID = BusinessLink[BusinessLink.rfind("-", 0)+1:len(BusinessLink)]
      print(BusinessID)
      BusinessSoup = GetSoup(BusinessLink)
      #ShowPrettySoup(BusinessLink)
      if len(BusinessSoup.find_all("span", class_="gz-cat"))>0:
        BusinessName = BusinessSoup.find_all("h1", class_="gz-pagetitle")[0].getText()
      else:
        BusinessName = "N/A"    
      print(BusinessName)

      if len(BusinessSoup.find_all("span", class_="gz-cat"))>0:
        BusinessCat = BusinessSoup.find_all("span", class_="gz-cat")[0].getText()
      else:
        BusinessCat = "N/A"    
      print(BusinessCat)

      #THERE ARE SOME ENTRIES THAT HAVE TWO ROWS FOR STREET ADDRESS
      #HAVE TO SET UP A CHECK FOR THAT.  PROBABLY JUST COMBINE THEM
      if len(BusinessSoup.find_all("span", class_="gz-street-address"))>0:
        StreetAddress = BusinessSoup.find_all("span", class_="gz-street-address")[0].getText()
      else:
        StreetAddress = "N/A"
      print(StreetAddress)

      if len(BusinessSoup.find_all("span", class_="gz-address-city"))>0:
        City = BusinessSoup.find_all("span", class_="gz-address-city")[0].getText()
      else:
        City = "N/A"
      print(City)

      if len(BusinessSoup.find_all(itemprop="addressRegion"))>0:
        Province = BusinessSoup.find_all(itemprop="addressRegion")[0].getText()
      else:
        Province = "N/A"
      print(Province)

      if len(BusinessSoup.find_all(itemprop="postalCode"))>0:
        PostalCode = BusinessSoup.find_all(itemprop="postalCode")[0].getText()
      else:
        PostalCode = "N/A"
      print(PostalCode)
      
      if len(BusinessSoup.find_all(itemprop="telephone"))>0:
        Telephone = BusinessSoup.find_all(itemprop="telephone")[0].getText()
      else:
        Telephone = "N/A"
      print(Telephone)
      
      if len(BusinessSoup.find_all(itemprop="faxNumber"))>0:
        FaxNumber = BusinessSoup.find_all(itemprop="faxNumber")[0].getText()
      else:
        FaxNumber = "N/A"
      print(FaxNumber)
      
      if len(BusinessSoup.find_all(itemprop="url", class_="card-link"))>0:
        BusinessUrlMessy = str(BusinessSoup.find_all(itemprop="url", class_="card-link")[0])
        BusinessUrl = BusinessUrlMessy[27:BusinessUrlMessy.find('"',28)]
      else:
        BusinessUrl = "N/A"
      print(BusinessUrl)
      
      NanaimoChamberCSV.writerow([BusinessID, BusinessName, BusinessCat, StreetAddress, City, Province, PostalCode, Telephone, FaxNumber, BusinessUrl])
      print("--------------------------------------------")
    writeFile.close
    