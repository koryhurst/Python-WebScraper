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
mycursor.execute("SELECT BusinessID, Website FROM tblbusiness")
myresult = mycursor.fetchall()

for BaseURL in myresult:
  #Just skipping it for now
  if BaseURL[1] != "http://www.ablerecognition.com":
    #wait = input("PRESS ENTER TO CONTINUE")
    print(BaseURL[1])
    BeautifulSoupFunctions.GetSiteMap(BaseURL[0], BaseURL[1], DatabaseDetails)
    
