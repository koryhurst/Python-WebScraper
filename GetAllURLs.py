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

ExceptionList = ["http://www.ablerecognition.com", "http://www.vi.bbb.org"]
mycursor = mydb.cursor()
mycursor.execute("SELECT BusinessID, WebSite FROM tblbusiness order by BusinessID")
myresult = mycursor.fetchall()
print(myresult)
for BaseURL in myresult:
  #Just skipping it for now
  if BaseURL[1] not in ExceptionList:
    #wait = input("PRESS ENTER TO CONTINUE")
    if BaseURL[1] != "N/A":
      print(BaseURL[1])
      BeautifulSoupFunctions.GetSiteMap(BaseURL[0], BaseURL[1], DatabaseDetails)
    
