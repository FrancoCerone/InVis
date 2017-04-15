'''
Created on 14 mar 2017

@author: francescocerone
'''


class ScreenResolution(object):
    
    def __init__(self):
        #mac
        self.width = 2560
        self.height = 1600
        #windos
        #self.width = 1366
        #self.height = 768 
    
    
    def get_width(self):
        return self.width;

    def get_height(self):
        return self.height;