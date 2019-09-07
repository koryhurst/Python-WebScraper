import mysql.connector
import sys
sys.path.append('../Python-FunctionLibrary')
import BeautifulSoupFunctions

DatabaseDetails = ["localhost","root","","dbkhurst"]

mydb = mysql.connector.connect(
  host=DatabaseDetails[0],
  user=DatabaseDetails[1],
  passwd=DatabaseDetails[2],
  database=DatabaseDetails[3]
  )

mycursor = mydb.cursor()
mycursor.execute("SELECT BusinessID, Website FROM tblbusiness where left(BusinessName,1) = 'a'")
myresult = mycursor.fetchall()

for BaseURL in myresult:
  #Just skipping it for now
  if BaseURL[1] != "http://www.ablerecognition.com":
    wait = input("PRESS ENTER TO CONTINUE")
    print(BaseURL[1])
    #wait = input("PRESS ENTER TO CONTINUE")
    #BeautifulSoupFunctions.ShowLinks(BaseURL[1])
    BeautifulSoupFunctions.GetSiteMap(BaseURL[0], BaseURL[1], DatabaseDetails)
    #for URL in AllUrlsOnASite:
    #  AllLinks.append((BaseURL[0],URL))
    #print(AllLinks)
    #mycursor.executemany(sql, AllLinks)
    #mydb.commit()
    #AllLinks.clear()
    #print(type(BaseURL))

