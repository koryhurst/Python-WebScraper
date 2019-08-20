
# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def GetLinkList(UrlToSearch, SearchTerm): #or searchtermSSSS at some point
  # Connect to the URL
  response = requests.get(UrlToSearch)
  #print(response.text)
  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(response.text, "html.parser")
  linklist = []
  # To download the whole data set, let's do a for loop through all a tags
  print(soup.findAll('a'))
  for i in range(36, len(soup.findAll('a')),1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    if SearchTerm in link:
      linklist.append(link)
  return linklist
#END FUNCTION GET LINKLIST	  

def ShowMePrettySoup(UrlToShow):
  response = requests.get(UrlToShow)
  #print(response.text)
  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(response.text, "html.parser")
  print(soup.prettify)

LinksToIndexPages = GetLinkList('https://members.nanaimochamber.bc.ca/list/','searchalpha')
for x in LinksToIndexPages:
  print(x)

ShowMePrettySoup(LinksToIndexPages[0])