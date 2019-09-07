import mysql.connector

DatabaseDetails = ["localhost","root","","dbkhurst"]

mydb = mysql.connector.connect(
  host=DatabaseDetails[0],
  user=DatabaseDetails[1],
  passwd=DatabaseDetails[2],
  database=DatabaseDetails[3]
  )

mycursorCheck = mydb.cursor()
sqlCheckThisPage = "select * from tblwebpage where URL = 'http://www.acecourier.bc.ca/\#content'"
mycursorCheck.execute(sqlCheckThisPage)
myresult = mycursorCheck.fetchall()
print(myresult)
#mycursorCheck.close()
print(mycursorCheck.rowcount)