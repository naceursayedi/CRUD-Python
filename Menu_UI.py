from tkinter import *
from tkinter import ttk
import Rgistration_UI
import Search_UI
def main_UI():

  root=Tk()
  root.title('University Database Management')

  register_Student=ttk.Button(root,text="Register Student")
  register_Student.grid(row=1,column=1,columnspan=2,ipadx=30,ipady=30,padx=50,pady=50)

  register_Student.config(command=lambda :Rgistration_UI.registration_Student_UI())

  register_Instructor = ttk.Button(root, text="Register Instructor")
  register_Instructor.grid(row=1, column=3, columnspan=2,ipadx=30,ipady=30,padx=50,pady=50)

  register_Instructor.config(command=lambda: Rgistration_UI.registration_Instructor_UI())

  register_Course = ttk.Button(root, text="Register Course")
  register_Course.grid(row=1, column=5, columnspan=2,ipadx=30,ipady=30,padx=50,pady=50)

  register_Course.config(command=lambda: Rgistration_UI.registration_Course_UI())

  register_TakeCourse = ttk.Button(root, text="Take Course")
  register_TakeCourse.grid(row=1, column=7, columnspan=2,ipadx=30,ipady=30,padx=50,pady=50)

  register_TakeCourse.config(command=lambda: Rgistration_UI.registration_TakeCourse_UI())

  Search = ttk.Button(root, text="Search")
  Search.grid(row=2, column=5, columnspan=2, ipadx=30, ipady=30, padx=50, pady=50)

  Search.config(command=lambda: Search_UI.search_UI())


  root.mainloop()



if __name__ == "__main__":main_UI()
