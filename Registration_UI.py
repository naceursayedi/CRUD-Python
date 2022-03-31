from tkinter import *
from tkinter import ttk
import Controller
from datetime import date
#import pandas as pd
import os
import os.path

def config_UI(titel,txt):
  registration_UI = Tk()
  registration_UI.title(titel)
  registration_UI.geometry('495x395')
  registration_UI.resizable(False, False)
  home_label = ttk.Label(registration_UI, text=txt, font=("Helvetica", 21)).grid(row=0, column=2,
                                                                                                     sticky="snew",
                                                                                                     padx=15, pady=15)
  return  registration_UI
def registration_Student_UI():
  registration_UI=config_UI('Register Student',"Student Registration ")

  vorname_label = ttk.Label(registration_UI, text="First Name  ").grid(row=1,column=0,sticky="snew",padx=10,pady=10)
  vorname=ttk.Entry(registration_UI,width=60)
  vorname.grid(row=1,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  nachname_label = ttk.Label(registration_UI, text="Last Name ").grid(row=2,column=0,sticky="snew",padx=10,pady=10)
  nachname=ttk.Entry(registration_UI,width=60)
  nachname.grid(row=2,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  address_label = ttk.Label(registration_UI, text="Address ").grid(row=3,column=0,sticky="snew",padx=10,pady=10)
  address=ttk.Entry(registration_UI,width=60)
  address.grid(row=3,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  zip_label = ttk.Label(registration_UI, text="Zip ").grid(row=4,column=0,sticky="snew",padx=10,pady=10)
  zip=ttk.Entry(registration_UI,width=10)
  zip.grid(row=4,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  city_label = ttk.Label(registration_UI, text="City ").grid(row=5,column=0,sticky="snew",padx=10,pady=10)
  city=ttk.Entry(registration_UI,width=20)
  city.grid(row=5,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  underGrad_label=ttk.Label(registration_UI, text="UnderGrad :").grid(row=6,column=0,sticky="snew",padx=10,pady=10)
  underGrad=ttk.Entry(registration_UI,width=20)
  underGrad.grid(row=6,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  register=ttk.Button(registration_UI,text="Register")
  register.grid(row=7,column=1,columnspan=2,ipadx=10,ipady=10,padx=10,pady=10)
  #register.config(command=lambda:Controller.registerStudent())

  register.config(command=lambda:Controller.register((vorname.get(), nachname.get(), address.get(), zip.get(), city.get(),date.today().strftime('%Y-%m-%d'), underGrad.get()),"Student"))

  registration_UI.mainloop()
def registration_Instructor_UI():
  registration_inst_UI=config_UI('Register Instructor',"Instructor Registration ")


  instName_label = ttk.Label(registration_inst_UI, text="Instructor Name ").grid(row=1,column=0,sticky="snew",padx=10,pady=10)
  instName=ttk.Entry(registration_inst_UI,width=60)
  instName.grid(row=1,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  instOffice_label = ttk.Label(registration_inst_UI, text="Instructor Office ").grid(row=2,column=0,sticky="snew",padx=10,pady=10)
  instOffice=ttk.Entry(registration_inst_UI,width=60)
  instOffice.grid(row=2,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  rank_label = ttk.Label(registration_inst_UI, text="Rank ").grid(row=3,column=0,sticky="snew",padx=10,pady=10)
  rank=ttk.Entry(registration_inst_UI,width=60)
  rank.grid(row=3,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  register=ttk.Button(registration_inst_UI,text="Register")
  register.grid(row=4,column=1,columnspan=2,ipadx=10,ipady=10,padx=10,pady=10)

  register.config(command=lambda:Controller.register((instName.get(), instOffice.get(), rank.get()),"Instructor"))


  registration_inst_UI.mainloop()
def registration_Course_UI():
  registration_course_UI = config_UI('Register Course',"Course Registration ")

  course_label = ttk.Label(registration_course_UI, text="Course ").grid(row=1,column=0,sticky="snew",padx=10,pady=10)
  course=ttk.Entry(registration_course_UI,width=60)
  course.grid(row=1,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  titel_label = ttk.Label(registration_course_UI, text="Titel ").grid(row=2,column=0,sticky="snew",padx=10,pady=10)
  titel=ttk.Entry(registration_course_UI,width=60)
  titel.grid(row=2,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  crHour_label = ttk.Label(registration_course_UI, text="Course Hours ").grid(row=3, column=0, sticky="snew", padx=10, pady=10)
  crHour = ttk.Entry(registration_course_UI, width=60)
  crHour.grid(row=3, column=1, columnspan=2, sticky="snew", padx=10, pady=10)

  instName_label = ttk.Label(registration_course_UI, text="Instructor Name ").grid(row=4,column=0,sticky="snew",padx=10,pady=10)
  instName=ttk.Entry(registration_course_UI,width=60)
  instName.grid(row=4,column=1,columnspan=2,sticky="snew",padx=10,pady=10)

  register=ttk.Button(registration_course_UI,text="Register")
  register.grid(row=5,column=1,columnspan=2,ipadx=10,ipady=10,padx=10,pady=10)
  register.config(command=lambda:Controller.register((course.get(),titel.get(),crHour.get(),instName.get()),"Course"))


  registration_course_UI.mainloop()

def registration_TakeCourse_UI():
  registration_take_course_UI = config_UI('Take Course',"Taking a Course ")

  student_label = ttk.Label(registration_take_course_UI, text="Student ").grid(row=1, column=0, sticky="snew", padx=10, pady=10)
  student = ttk.Entry(registration_take_course_UI, width=60)
  student.grid(row=1, column=1, columnspan=2, sticky="snew", padx=10, pady=10)

  course_label = ttk.Label(registration_take_course_UI, text="Course ").grid(row=2,column=0,sticky="snew",padx=10,pady=10)
  course=ttk.Entry(registration_take_course_UI,width=60)
  course.grid(row=2,column=1,columnspan=2,sticky="snew",padx=10,pady=10)


  register=ttk.Button(registration_take_course_UI,text="Take")
  register.grid(row=3,column=1,columnspan=2,ipadx=10,ipady=10,padx=10,pady=10)
  register.config(command=lambda:Controller.register((student.get(),course.get()),"Take a Course"))


  registration_take_course_UI.mainloop()
