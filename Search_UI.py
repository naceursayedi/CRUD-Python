from tkinter import *
from tkinter import ttk
import tkinter as tk
import Controller

def show(s1):
    print(s1)
def search_Config_UI():

    search_UI=Tk()
    search_UI.title('Search')
    return search_UI
def add(val):
    print(val)
    return val
def search_Input(root):
    #Frame Input configuration
    frame_Input = ttk.Frame(root)
    frame_Input.pack()
    frame_Input.config(height=500,relief=RIDGE)

    selected = StringVar()
    search_UI = ttk.Combobox(frame_Input, textvariable=selected)
    search_UI['values'] = ("student", "instructor","course","take")
    search_UI['state'] = 'readonly'
    search_UI.grid(row=1, column=0, columnspan=2, ipadx=30, ipady=30, padx=30, pady=30)

    id_label = ttk.Label(frame_Input, text="ID : ").grid(row=2, column=0, sticky="snew", padx=10, pady=10)
    id = ttk.Entry(frame_Input, width=60)
    id.grid(row=2, column=1, columnspan=2, sticky="snew", padx=10, pady=10)

    search = ttk.Button(frame_Input, text="Search")
    search.grid(row=2, column=3, columnspan=2, ipadx=10, ipady=10, padx=10, pady=10)
    search.config(command=lambda:Controller.search(selected.get(),id.get()))

    searchAll = ttk.Button(frame_Input, text="Search All")
    searchAll.grid(row=3, column=3, columnspan=2, ipadx=10, ipady=10, padx=10, pady=10)
    searchAll.config(command=lambda:Controller.search(selected.get(),"all"))


def search_UI():
    root = search_Config_UI()
    search_Input(root)
    root.mainloop()

if __name__ == "__main__":search_UI()
