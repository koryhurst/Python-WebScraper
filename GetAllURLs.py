import mysql.connector
import sys
sys.path.append('../Python-FunctionLibrary')
import BeautifulSoupFunctions

DatabaseDetails = ["localhost","root","","dbkhurst"]

mydb = mysql.connector.connect(
  host=DatabaseDetail[1],
  user=DatabaseDetail[2],
  passwd=DatabaseDetail[3],
  database=DatabaseDetail[4]
  )

mydb = mysql.connector.connect(

mycursor = mydb.cursor()
mycursor.execute("SELECT BusinessID, Website FROM tblbusiness where left(BusinessName,1) = 'a'")
myresult = mycursor.fetchall()

for BaseURL in myresult:
  #Just skipping it for now
  if BaseURL[1] != "http://www.ablerecognition.com":
    print(BaseURL[1])
    #wait = input("PRESS ENTER TO CONTINUE")
    BeautifulSoupFunctions.ShowLinks(BaseURL[1])
    AllUrlsOnASite = BeautifulSoupFunctions.GetSiteMap(BaseURL[1], DatabaseDetails)
    for URL in AllUrlsOnASite:
      AllLinks.append((BaseURL[0],URL))
    print(AllLinks)
    mycursor.executemany(sql, AllLinks)
    mydb.commit()
    AllLinks.clear()
    #print(type(BaseURL))

