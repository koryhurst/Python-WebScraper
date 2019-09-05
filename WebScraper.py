
# Import libraries
import csv
import sys

#sys.path.append('D:/Users/Kory/Documents/_HomeAndWork/GitHub/Python-FunctionLibrary')
sys.path.append('../Python-FunctionLibrary')
import BeautifulSoupFunctions
import ListFunctions

LinksToIndexPages = BeautifulSoupFunctions.GetLinkListOLD('https://members.nanaimochamber.bc.ca/list/','searchalpha')
with open('NanaimoChamber.csv', mode='w') as writeFile:
  NanaimoChamberCSV = csv.writer(writeFile, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
  for IndexPage in LinksToIndexPages:
    #print(IndexPage)
    LinksToBusinesPages = BeautifulSoupFunctions.GetLinkListOLD(IndexPage,'t/member/')  
    for BusinessLink in ListFunctions.RemoveDupesFromList(LinksToBusinesPages):
      #print(BusinessLink)
      BusinessID = BusinessLink[BusinessLink.rfind("-", 0)+1:len(BusinessLink)]
      print(BusinessID)
      BusinessSoup = BeautifulSoupFunctions.GetSoup(BusinessLink)
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
    