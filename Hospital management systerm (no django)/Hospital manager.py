# Welton Addra
# Date: 12/20/2022
# IMPORTANT COMMENT!!!!:  Before running code, please go to your terminal and type: "pip install tk" and "pip install customtkinter" if those do not work, run the same commands but with python -m at the beguinning 
# This program is a managment system for regulating hospital patients and workers

from tkinter import *
import customtkinter
import sqlite3
import random

root = customtkinter.CTk()
root.geometry("800x600")
customtkinter.set_appearance_mode("System")
root.title("Hospital management")


def clear_window():
    for widgets in root.winfo_children():
        widgets.destroy()

def welcome():
    welcomeText = customtkinter.CTkTextbox(root,width=700,font=customtkinter.CTkFont(size=30),wrap=WORD)
    welcomeText.grid(row=0,column=0)
    welcomeText.place(relx=0.5,rely=0.05,anchor=N)


    patientButton = customtkinter.CTkButton(master=root, text="Patients",hover_color="green", command= lambda:[patients(), clear_window()])
    patientButton.place(relx=0.4, rely=0.5, anchor=CENTER)

    workerButton = customtkinter.CTkButton(master=root, text="Workers",hover_color="green",command= lambda: [workers(),clear_window()])
    workerButton.place(relx=0.6, rely=0.5, anchor=CENTER)


    welcomeText.insert("0.0","""Welcome to HMS, the Hospital Managment System. The purpose of this application is to manage hospital patients and workers. The system is designed to be easy to use.""")
    welcomeText.configure(state="disabled")
    

    #root.mainloop()
 


def patients():
    panel1 = PanedWindow(bd=4,relief="raised",bg="gray")

    allPatientsBtn = customtkinter.CTkButton(master=root, text="All patients",hover_color="green", command=allPatients)
    allPatientsBtn.place(relx=0.4, rely=0.5, anchor=CENTER)

    addPatientsBtn = customtkinter.CTkButton(master=root, text="Add patients",hover_color="green", command=addPatients)
    addPatientsBtn.place(relx=0.6, rely=0.5, anchor=CENTER)

    rmvPatientsBtn = customtkinter.CTkButton(master=root, text="Remove patients",hover_color="green", command=rmvPatients)
    rmvPatientsBtn.place(relx=0.8, rely=0.5, anchor=CENTER)

    #root.mainloop()

    





def allPatients():
    car = "carssss"
    print(f"all{car}")

def addPatients():
    print("add")

def rmvPatients():
    print("rmv")


def workers():
    print("Workers")


def showTable():
    something = 0 


if __name__ == '__main__':
    global conn
    conn = sqlite3.connect('HMS.db')
    global c 
    c = conn.cursor()
    global admin
    admin = False
    welcome()

while True:
    root.mainloop()