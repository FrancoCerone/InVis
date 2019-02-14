'''
Created on Feb 12, 2019

@author: franco
'''


class LogoStrip(object):
    indexStart = 0 
    length = 0
    def __init__(self, start, stripLength):
        self.indexStart = start
        self.length = stripLength
    
    def get_indexStart(self):
        return self.indexStart
    
    def get_length(self):
        return self.length
    
    
    def get_indexEnd(self):
        return self.indexStart + self.length -1;

class Logo(object):
    stripList= []
    def __init__(self):
        strip1 = LogoStrip(1,57)
        self.stripList.append(strip1)
        
        strip2 = LogoStrip(strip1.get_indexEnd()+1,44)
        self.stripList.append(strip2)
        
        strip3 = LogoStrip(strip2.get_indexEnd()+1,7)
        self.stripList.append(strip3)
        
        strip4 = LogoStrip(strip3.get_indexEnd()+1,105)
        self.stripList.append(strip4)
        
        strip5 = LogoStrip(strip4.get_indexEnd()+1,7)
        self.stripList.append(strip5)
        
        strip6 = LogoStrip(strip5.get_indexEnd()+1,44)
        self.stripList.append(strip6)
        
        strip7 = LogoStrip(strip6.get_indexEnd()+1,37)
        self.stripList.append(strip7)
        
        strip8 = LogoStrip(strip7.get_indexEnd()+1,7)
        self.stripList.append(strip8)
        
        strip9 = LogoStrip(strip8.get_indexEnd()+1,14)
        self.stripList.append(strip9)
        
        strip10 = LogoStrip(strip9.get_indexEnd()+1,6)
        self.stripList.append(strip10)
        
        strip11 = LogoStrip(strip10.get_indexEnd()+1,14)
        self.stripList.append(strip11)
        
        strip12 = LogoStrip(strip11.get_indexEnd()+1,18)
        self.stripList.append(strip12)
        
        srip13 = LogoStrip(strip12.get_indexEnd()+1,8)
        self.stripList.append(srip13)
        
        strip14 = LogoStrip(srip13.get_indexEnd()+1,36)
        self.stripList.append(strip14)
        
        strip15 = LogoStrip(strip14.get_indexEnd()+1,43)
        self.stripList.append(strip15)
        
        strip16 = LogoStrip(strip15.get_indexEnd()+1,8)
        self.stripList.append(strip16)
        
        strip17 = LogoStrip(strip16.get_indexEnd()+1,13)
        self.stripList.append(strip17)
        
        strip18 = LogoStrip(strip17.get_indexEnd()+1,8)
        self.stripList.append(strip18)
                
        strip19 = LogoStrip(strip18.get_indexEnd()+1,17)
        self.stripList.append(strip19)
        
        strip20 = LogoStrip(strip19.get_indexEnd()+1,9)
        self.stripList.append(strip20)
        
        strip21 = LogoStrip(strip20.get_indexEnd()+1,13)
        self.stripList.append(strip21)
        
        strip22 = LogoStrip(strip21.get_indexEnd()+1,36)
        self.stripList.append(strip22)
        
        strip23 = LogoStrip(strip22.get_indexEnd()+1,37)
        self.stripList.append(strip23)
        
        strip24 = LogoStrip(strip23.get_indexEnd()+1,46)
        self.stripList.append(strip24)
        
        strip25 = LogoStrip(strip24.get_indexEnd()+1,28)
        self.stripList.append(strip25)
        
        strip26 = LogoStrip(strip25.get_indexEnd()+1,6)
        self.stripList.append(strip26)
        
        strip27 = LogoStrip(strip26.get_indexEnd()+1,14)
        self.stripList.append(strip27)
        
        strip28 = LogoStrip(strip27.get_indexEnd()+1,8)
        self.stripList.append(strip28)
        
        strip29 = LogoStrip(strip28.get_indexEnd()+1,18)
        self.stripList.append(strip29)
        
        strip30 = LogoStrip(strip29.get_indexEnd()+1,7)
        self.stripList.append(strip30)
        
        strip31 = LogoStrip(strip30.get_indexEnd()+1,14)
        self.stripList.append(strip31)
        
    def get_border_index(self):
        borderStrip = []
        borderStrip.append(self.stripList[0])
        borderStrip.append(self.stripList[1])
        borderStrip.append(self.stripList[2])
        borderStrip.append(self.stripList[3])
        borderStrip.append(self.stripList[4])
        borderStrip.append(self.stripList[5])
        return self.getIndex(borderStrip)

    def get_border_eyes_mouth_index(self):
        strips = []
        strips.append(self.stripList[0])
        strips.append(self.stripList[1])
        strips.append(self.stripList[2])
        strips.append(self.stripList[3])
        strips.append(self.stripList[4])
        strips.append(self.stripList[5])
        strips.append(self.stripList[28])
        strips.append(self.stripList[30])
        strips.append(self.stripList[26])
        strips.append(self.stripList[18])
        strips.append(self.stripList[20])
        strips.append(self.stripList[16])
        strips.append(self.stripList[11])
        strips.append(self.stripList[10])
        strips.append(self.stripList[8])
        return self.getIndex(strips)
    
    def get_eyes_strips_index(self):
        strips = []
        strips.append(self.stripList[28])
        strips.append(self.stripList[30])
        strips.append(self.stripList[26])
        strips.append(self.stripList[18])
        strips.append(self.stripList[20])
        strips.append(self.stripList[16])
        return self.getIndex(strips)

    
    def get_eyes_and_mounth_strips_index(self):
        strips = []
        strips.append(self.stripList[28])
        strips.append(self.stripList[30])
        strips.append(self.stripList[26])
        strips.append(self.stripList[18])
        strips.append(self.stripList[20])
        strips.append(self.stripList[16])
        strips.append(self.stripList[11])
        strips.append(self.stripList[10])
        strips.append(self.stripList[8])
        return self.getIndex(strips)
    
    def get_allSripIndex(self):
        return self.getIndex(self.stripList)
    
    
    
              
    def get_number_of_leds(self):
        return self.stripList[-1].get_indexEnd()   
        
    def get_allSrip(self):
        return self.stripList;
    
    def getIndex(self, selectedstripList):
        indexs = []
        print "numero di strisce:", selectedstripList.__len__()
        for logoStrip in  selectedstripList:
            print "index Start", logoStrip.get_indexStart()
            index =logoStrip.get_indexStart()
            while index <= logoStrip.get_indexEnd():
                indexs.append(index - 1)
                index = index+1
        return indexs   
        

if __name__ == '__main__':
    logo = Logo();
    logo.get_allSrip();
    
    
    
    print logo.getIndex(logo.get_eyes_and_mounth_strips())
    
    
    
    
    
    '''
    for strip in logo.get_allSrip():
        print strip.get_indexStart()
    
    indexs = logo.getIndex(logo.get_allSrip())
    print 'tutto gli indici', indexs
    list = [] 
    list.append(logo.get_allSrip()[0])
    print 'prima strisca', logo.getIndex(list)
    list = [] 
    list.append(logo.get_allSrip()[1])
    print 'seconda strisca', logo.getIndex(list)
    list = []
    list.append(logo.get_allSrip()[2])
    print 'terza strisca', logo.getIndex(list)
    print "ultimo elemento" , logo.get_number_of_leds()
    '''
    print "prima striscia", logo.get_allSrip()[0]
    