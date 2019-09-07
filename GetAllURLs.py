import mysql.connector
import sys
sys.path.append('../Python-FunctionLibrary')
import BeautifulSoupFunctions

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="dbkhurst"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT BusinessID, Website FROM tblbusiness where left(BusinessName,1) = 'a'")
myresult = mycursor.fetchall()

sql = "INSERT INTO tblwebpage (BusinessID, URL) VALUES (%s, %s)"
AllLinks = []
  
for BaseURL in myresult:
  #Just skipping it for now
  if BaseURL[1] != "http://www.ablerecognition.com":
    print(BaseURL[1])
    #wait = input("PRESS ENTER TO CONTINUE")
    BeautifulSoupFunctions.ShowLinks(BaseURL[1])
    AllUrlsOnASite = BeautifulSoupFunctions.GetSiteMap(BaseURL[1])
    for URL in AllUrlsOnASite:
      AllLinks.append((BaseURL[0],URL))
    print(AllLinks)
    mycursor.executemany(sql, AllLinks)
    mydb.commit()
    AllLinks.clear()
    #print(type(BaseURL))

