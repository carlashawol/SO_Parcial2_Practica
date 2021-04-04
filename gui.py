import socket
import os
from datetime import datetime
from datetime import date
from os import path
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
from random import randrange
import time
import subprocess



PORT = 8000
FORMAT = "utf-8"
HOST = "localhost" 
gui_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR= (HOST,PORT)
gui_send.connect(ADDR)
print("GUI binded to port: 8000 and host: localhost.....listening")

msg="Gui"
gui_send.send(msg.encode(FORMAT))

def open_calculator():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERRR"

    default_message = "status:"+strstatus+",cmd:info,src:GUI,dst:Application,pid:"+str(os.getpid())+",msg:'\log: " + current_time + " "+ current_date+ ",OPEN CALCULATOR"
    message = default_message.encode(FORMAT)
    gui_send.send(message)

def open_excel():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERROR"

    default_message = "status:"+strstatus+",cmd:info,src:GUI,dst:Application,pid:"+str(os.getpid())+",msg:'\log: " + current_time + " "+ current_date+ ",OPEN EXCEL"
    message = default_message.encode(FORMAT)
    gui_send.send(message)

def open_word():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERROR"

    default_message = "status:"+strstatus+",cmd:info,src:GUI,dst:Application,pid:"+str(os.getpid())+",msg:'\log: " + current_time + " "+ current_date+ ",OPEN WORD"
    message = default_message.encode(FORMAT)
    gui_send.send(message)

def close_calculator():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERROR"
    
    default_message = "status:"+strstatus+",cmd:info,src:GUI,dst:Application,pid:"+str(str(os.getpid()))+",msg:'\log: " + current_time + " "+ current_date + ",CLOSE CALCULATOR"
    message = default_message.encode(FORMAT)
    gui_send.send(message)

def close_excel():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERROR"
    
    default_message = "status:"+strstatus+",cmd:info,src:GUI,dst:Application,pid:"+str(str(os.getpid()))+",msg:'\log: " + current_time + " "+ current_date + ",CLOSE EXCEL"
    message = default_message.encode(FORMAT)
    gui_send.send(message)

def close_word():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERROR"
    
    default_message = "status:"+strstatus+",cmd:info,src:GUI,dst:Application,pid:"+str(str(os.getpid()))+",msg:'\log: " + current_time + " "+ current_date + ",CLOSE WORD"
    message = default_message.encode(FORMAT)
    gui_send.send(message)                 


def folder_popup():
    open_new_window = tk.Toplevel(window)
    open_new_window.title("MF")
    folder_lable = tk.Label(open_new_window, text = ' Insert folder name:', font = ('Courier',10,'bold'))
    open_new_window.config(background = "pink" )
    folder_name = ttk.Entry(open_new_window, width=30)
    create_boton = tk.Button(open_new_window, text= "Create Folder",bg="white", font=("Courier", 10), command = lambda: make_folder(folder_name.get()))
    delete_boton = tk.Button(open_new_window, text= "Delete Folder",bg="white", font=("Courier", 10), command = lambda: delete_folder(folder_name.get()))
    open_new_window.geometry("300x150")
    folder_lable.pack(padx=10, pady=10)
    folder_name.pack()
    create_boton.pack()
    delete_boton.pack()

def app_popup():
    open_new_window2 = tk.Toplevel(window)
    open_new_window2.title("App Manager")
    create_lable = tk.Label(open_new_window2, text="Open Applications", fg="black", font=("Courier", 15), bg = "pink1")
    create_lable2 = tk.Label(open_new_window2, text="Close Applications", fg="black", font=("Courier", 15), bg = "pink1")
    open_new_window2.config(background = "pink" )
    create_boton = tk.Button(open_new_window2, text= "Open Excel",font=("Courier", 10), command = open_excel, bg="white")
    create_boton2 = tk.Button(open_new_window2, text= "Open Word",font=("Courier", 10), command = open_word, bg="white")
    create_boton3 = tk.Button(open_new_window2, text= "Open Calculator",font=("Courier", 10), command = open_calculator, bg="white")
    create_boton4 = tk.Button(open_new_window2, text= "Close Calculator",font=("Courier", 10), command = close_calculator, bg="white")
    create_boton5 = tk.Button(open_new_window2, text= "Close Excel",font=("Courier", 10), command = close_excel, bg="white")
    create_boton6 = tk.Button(open_new_window2, text= "Close Word",font=("Courier", 10), command = close_word, bg="white")
    open_new_window2.geometry("300x300")
    create_lable.pack()
    create_boton.pack()
    create_boton2.pack()
    create_boton3.pack()
    create_lable2.pack()
    create_boton5.pack()
    create_boton6.pack()
    create_boton4.pack()


def make_folder(folder_name):
    if folder_name != "":
        if path.exists(folder_name):
            pass
        else: 
            now = datetime.now()
            today = date.today()
            current_time = now.strftime("%H:%M:%S")
            current_date = today.strftime("%d/%m/%Y")
            status=randrange(1,10)

            if(status>=1 and status<=7):
                strstatus="PROC" 
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERRR" 
            
            default_message = "status:"+strstatus+",cmd:send,src:GUI,dst:FileManager,msg:'\log: " + current_time + " "+ current_date + " CREATE FOLDER: "+folder_name
            message = default_message.encode(FORMAT)
            gui_send.send(message)

def delete_folder(folder_name):
    if folder_name != "":
        if path.exists(folder_name):
            now = datetime.now()
            today = date.today()
            current_time = now.strftime("%H:%M:%S")
            current_date = today.strftime("%d/%m/%Y")
            status=randrange(1,10)       
            
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERRR"
            
            default_message = "status:"+strstatus+",cmd:send,src:GUI,dst:FileManager,msg:'\log: " + current_time + " "+ current_date + " DELETE FOLDER: "+ folder_name
            message = default_message.encode(FORMAT)
            gui_send.send(message)


def backup_logs_read():
    logs_here.delete('1.0',END)
    back_up_file = open("logs_backup.txt", 'r')
    log_information = back_up_file.read()
    logs_here.insert(tk.END, log_information)
    logs_here.after(1000, backup_logs_read)
    back_up_file.close()

def close_system():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    status=randrange(1,10)       
            
    if(status>=1 and status<=7):
        strstatus="PROC"
    elif(status==8 or status==9):
        strstatus="BUSY"
    elif(status==10):
        strstatus="ERRR"
    
    default_message = "status:"+strstatus+",cmd:stop,src:GUI,dst:Kernel,msg:'\log: " + current_time + " "+ current_date + " STOP SYSTEM"
    message = default_message.encode(FORMAT)
    gui_send.send(message)
    time.sleep(2)
    quit()



window = Tk()

window.title("Proyecto")
window.state('zoomed')
window.config(background = "pink" )


wrapper1 = LabelFrame(window)
wrapper2 = LabelFrame(window)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT)


myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")
wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

f = open ('logs_backup.txt','wb')
f.close()

logs_history_label = tk.Label(wrapper1, text="Logs History", fg="black", font=("Courier", 15),bg = "pink1")
logs_history_label.config(background = "pink")

logs_history_label.pack()

logs_here = scrolledtext.ScrolledText(wrapper1, width=105, height=32)
logs_here.pack()


backup_logs_read()

create_boton = tk.Button(wrapper2, text= "App Manager",font=("Courier", 15), command = app_popup,  bg = "pink1")
create_boton.pack(side=LEFT, padx=10, pady=10)
create_boton1 = tk.Button(wrapper2,text= "File Manager",font=("Courier", 15), command = folder_popup,  bg = "pink1")
create_boton1.pack(side=LEFT, padx=10, pady=10)
create_boton2 = tk.Button(wrapper2,text= "CLOSE SYSTEM",font=("Courier", 15), command = close_system,  bg = "pink1")
create_boton2.pack(side=LEFT, padx=10, pady=10)

window.mainloop()




