#!/usr/bin/env python3

##import necessary modules
import time
import socket

## use an  ongoing while loop to generate output
while True :

##set the hostname and current date 
    host = socket.gethostname()
    date = time.strftime("%y-%m-%d %H:%M%:S")

## convert the date output to a string 
    now = str(date)
##  open the named file   date in append mode
## append the output of hostname and time 
    f = open("date.out", "a")
    f.write(now + "\n")
    f.write(host + "\n")
    f.close()

## sleep for five seconds the continue the loop
    time.sleep(5)

