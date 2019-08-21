
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
    print(BusinessLink)

#<a href="https://members.nanaimochamber.bc.ca/list/member/edgewood-232" target="_blank" alt="Edgewood">
#                <span class="gz-img-placeholder">Edgewood</span>
#            </a>
			


#ShowMeLinks(LinksToIndexPages[0])
#ShowMePrettySoup(LinksToIndexPages[0])