import socket
import os
from datetime import datetime
from datetime import date
from os import path
import subprocess
from random import randrange
import time
pid = os.getpid() #Process ID


PORT   = 8000
FORMAT = "utf-8"
HOST = "localhost"

app_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR= (HOST,PORT)
app_send.connect(ADDR)
print("GUI binded to port: 8000 and host: localhost.....listening")

msg="App"
app_send.send(msg.encode(FORMAT))

opened_processes = []

while True: 
    msg = app_send.recv(1024).decode(FORMAT)  
    print(msg)
    back_up_file = open("logs_backup.txt", 'a')
    back_up_file.write(msg+"\n")
    back_up_file.close()
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%d/%m/%Y")
    messageArray= msg.split(",")
    print("MSG ARRAY:", messageArray)
    if(messageArray[0]=="status:BUSY" or messageArray[0]=="status:PROC"):
        if(messageArray[1]=="cmd:stop"):

            os.system("taskkill /f /im calculator.exe")
            os.system("taskkill /f /im winword.exe")
            os.system("taskkill /f /im excel.exe")
            quit()

        if(messageArray[-1]=="OPEN CALCULATOR"):
            
            os.system("calc")
            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:FileManager,msg:'\log: " + current_time + " "+ current_date+ "--> CALCULATOR OPENED"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)


        elif(messageArray[-1]=="CLOSE CALCULATOR"):

            os.system("taskkill /f /im calculator.exe")

            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:FileManager,msg:'\log: " + current_time + " "+ current_date + "--> CALCULATOR CLOSED"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)

        elif(messageArray[-1]=="OPEN EXCEL"):

            os.system("start excel") 
            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:FileManager,msg:'\log: " + current_time + " "+ current_date + "--> EXCEL OPENED"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)

        elif(messageArray[-1]=="CLOSE EXCEL"):

            os.system("taskkill /f /im excel.exe")

            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:FileManager,msg:'\log: " + current_time + " "+ current_date + "--> EXCEL CLOSED"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)

        elif(messageArray[-1]=="OPEN WORD"):

            os.system("start winword")
            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:FileManager,msg:'\log: " + current_time + " "+ current_date + "--> WORD OPENED"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)

        elif(messageArray[-1]=="CLOSE WORD"):

            os.system("taskkill /f /im winword.exe")
            status=randrange(1,10)
            if(status>=1 and status<=7):
                strstatus="PROC"
            elif(status==8 or status==9):
                strstatus="BUSY"
            elif(status==10):
                strstatus="ERROR"

            msg="status:"+strstatus+",cmd:send,src:Application,dst:FileManager,msg:'\log: " + current_time + " "+ current_date + "--> WORD CLOSED"
            msg_send=msg.encode(FORMAT)
            app_send.send(msg_send)
    
    elif(messageArray[0]=="status:ERRR"):
        if(messageArray[1]=="cmd:stop"):
            os.system("taskkill /f /im calculator.exe")
            os.system("taskkill /f /im winword.exe")
            os.system("taskkill /f /im excel.exe")
            quit()

        os.system("taskkill /f /im calculator.exe")
        os.system("taskkill /f /im winword.exe")
        os.system("taskkill /f /im excel.exe")
        print("CLOSE APPS BY ERROR....")

       