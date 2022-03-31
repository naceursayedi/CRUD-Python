from tkinter import messagebox
import connectDb





#Registration
def register(data,type):
    if type=="Student":
        req="INSERT INTO student(LastName,FirstName,Address,Zip,City,EnrollDate,UnderGrad) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    elif type == "Instructor":
        req = "INSERT INTO instructor(InstName,InstOffice,Rank) VALUES (%s,%s,%s)"
    elif type == "Course":
        req = "INSERT INTO course(Course,Title,CrHour,InstName) VALUES (%s,%s,%s,%s)"
    else:
        req = "INSERT INTO take(Student,Course) VALUES (%s,%s)"

    result=connectDb.crud_Data(data,req)

    if (result.rowcount >= 1):
        messagebox.showinfo("Registration "+type, "you are registered")

#Search
def search(typeselected,data):

    if(data=="all"):
        req="SELECT * FROM "+typeselected+";"
    elif(typeselected=="student"):
        req = 'SELECT * FROM ' + typeselected + ' WHERE Student="' + data + '";'
        print(req)
    elif (typeselected == "course"):
        req = 'SELECT * FROM ' + typeselected + ' WHERE Course="' + data + '";'
    elif (typeselected == "instructor"):
        req = 'SELECT * FROM ' + typeselected + ' WHERE InstName="' + data + '";'
    elif (typeselected == "take"):
        #In Developement
        req='SELECT s.Student, s.FirstName, s.LastName, c.Title, c.InstName FROM student AS s, course AS c WHERE s.Student="' + data +'";'


    mycursor=connectDb.crud_Data(data,req)
    for x in mycursor:
        print(x)



