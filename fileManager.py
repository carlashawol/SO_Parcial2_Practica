import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import socket
import os 
from datetime import datetime
from datetime import date
from random import randrange

pid = os.getpid() #Process ID

PORT   = 8000
FORMAT = "utf-8"
HOST = "localhost" #Nombre e IP de ntro pc


logs_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR= (HOST,PORT)
logs_send.connect(ADDR)

print("GUI binded to port: 8000 and host: localhost.....listening")
msg="FileManager"
logs_send.send(msg.encode(FORMAT))

def backup_logs_read():
    back_up_file = open("logs_backup.txt", 'r')
    log_information = back_up_file.read()
    print(log_information)
    log_information = ""
    back_up_file.close()


def backup_logs_write(log):
    back_up_file = open("logs_backup.txt", 'a')
    back_up_file.write(log+"\n")
    back_up_file.close()

def create_or_delete_folder(msg):  
    if "CREATE FOLDER" in msg: 
        foldername = msg[91:]
        print(foldername)
        os.mkdir(foldername)
    elif "DELETE FOLDER" in msg:
        foldername = msg[91:]
        print(foldername)
        os.rmdir(foldername)
    else:
        pass
def check_close_program(msg):
    if "stop" in msg:
        quit()

while True:
    msg = logs_send.recv(1024).decode()  
    print(msg)
    create_or_delete_folder(msg)
    backup_logs_write(msg)
    check_close_program(msg)