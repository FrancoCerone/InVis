'''
Created on 14 mar 2017

@author: francescocerone
'''
class ScreenResolution(object):
    
    def __init__(self):
        self.width = 1366
        self.height = 768 
    
    
    @classmethod
    def get_width(self):
        return self.width;
    @classmethod
    def get_height(self):
        return self.height;