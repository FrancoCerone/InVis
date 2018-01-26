'''
Created on 26 gen 2018

@author: francescocerone
'''
### Server
import socket
from threading import *
import socket
import pygame
import pygame.camera
from pygame.locals import *
 
 
def server():
    try:
        #print "\nServer started at " + str(socket.gethostbyname(socket.gethostname())) + " at port " + str(90)  
        port = 8085
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(("", 8085 ))
        serversocket.listen(10)
        pygame.camera.init()
        cam = pygame.camera.Camera("/dev/video0",(640,480),"RGB")
        cam.start()
        img = pygame.Surface((640,480))
        while True:
            connection, address = serversocket.accept()
            print "GOT_CONNECTION"
            cam.get_image(img)
            data = pygame.image.tostring(img,"RGB")
            connection.sendall(data)
            connection.close()
    except Exception,e:
        print str(e)
        pass
 
server()