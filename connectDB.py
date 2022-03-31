from tkinter import messagebox

import mysql.connector


#Connect to db
def connectdb():
  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="university_db"
  )
  return mydb


def crud_Data(data,req):
  mydb=connectdb()
  mycursor = mydb.cursor()
  if(type(data) is str):
    mycursor.execute(req)
    searched = mycursor.fetchall()
    return searched
  else:
    mycursor.execute(req,data)
    mydb.commit()
    return mycursor
  mydb.close()




