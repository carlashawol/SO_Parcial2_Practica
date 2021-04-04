import os
from os import sys
import socket 
import threading 
import os
import os.path
import subprocess
import time
from random import randrange
from datetime import datetime
from datetime import date


PORT = 8000
FORMAT = "utf-8"
HOST = "localhost"
ADDR = (HOST, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = {}
arrCon = []
appbool = False
guibool = False
filebool = False
#INITIALIZATION
subprocess.Popen(["python", "gui.py"])
subprocess.Popen(["python", "fileManager.py"])
subprocess.Popen(["python", "application.py"])
#EXECUTION
def client_req(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    global appbool, guibool, filebool
    
    while True:
        msg = None
        try:
            msg=conn.recv(1024).decode(FORMAT)
        except:
            print("Error receiving")

        if appbool == False or guibool == False or filebool== False:
            if msg.startswith("App") and appbool == False:
                appbool=True
                print("APP CONNECTED")
                connections["App"]= conn
            elif msg.startswith("Gui") and guibool== False:
                guibool=True
                print("GUI CONNECTED")
                connections["Gui"]= conn
            elif msg.startswith("FileManager") and filebool==False:
                filebool=True
                print("FILE MANAGER CONNECTED")
                connections["FileManager"]= conn
        else:
            msg_array = msg.split(',')
            print("MSG ARRAY KERNEL:", msg_array)
            status=msg_array[0]
            target = msg_array[3]
            cmd = msg_array[1]
            if(status=="status:PROC"):
                if(cmd == "cmd:stop"):
                    close_system()
                if (target == "dst:Application"):
                    destino=connections["App"]
                    message = msg.encode(FORMAT) 
                    destino.send(message)
                elif(target == "dst:FileManager"):
                    message = msg.encode(FORMAT)                 
                    destino=connections["FileManager"]
                    destino.send(message)      
            elif(status=="status:BUSY"):    
                timeWait=randrange(1,3)
                print("WAITING "+str(timeWait)+" SECONDS....")
                time.sleep(timeWait)
                if(cmd == "cmd:stop"):
                    close_system()
                if (target == "dst:Application"):
                    destino=connections["App"]
                    message = msg.encode(FORMAT) 
                    destino.send(message)
                elif(target == "dst:FileManager"):
                    message = msg.encode(FORMAT)                 
                    destino=connections["FileManager"]
                    destino.send(message)
            elif(status=="status:ERRR"):
                if(cmd == "cmd:stop"):
                    close_system()
                destino=connections["App"]
                message = msg.encode(FORMAT) 
                destino.send(message)

#FINALIZATION
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
    default_message = "status:"+strstatus+",cmd:stop,src:kernel,dst:ALL,msg:'\log: " + current_time + " "+ current_date + " STOP SYSTEM"
    msg = default_message.encode(FORMAT)
    connections["App"].send(msg)
    connections["FileManager"].send(msg)
    time.sleep(3)
    server.shutdown(socket.SHUT_WR)  
    server.close()
    quit()
    

def start():
    server.listen()
    print(f"server is listenning on {HOST}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_req, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("Server is starting")
start()

