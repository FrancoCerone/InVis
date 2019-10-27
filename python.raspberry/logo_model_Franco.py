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
    
    def get_really_indexStart(self):
        return self.indexStart -1
        
    def get_length(self):
        return self.length
    
    
    def get_indexEnd(self):
        return self.indexStart + self.length -1;
    
    def get_really_indexEnd(self):
        return self.indexStart + self.length -2;
    
    
class LogoFranco(object):
    stripList= []
    def __init__(self):
        strip1 = LogoStrip(1,52)
        self.stripList.append(strip1)
        
        strip2 = LogoStrip(strip1.get_indexEnd()+1,52)
        self.stripList.append(strip2)
        
        strip3 = LogoStrip(strip2.get_indexEnd()+1,52)
        self.stripList.append(strip3)
        
        strip4 = LogoStrip(strip3.get_indexEnd()+1,52)
        self.stripList.append(strip4)
        
        strip5 = LogoStrip(strip4.get_indexEnd()+1,52)
        self.stripList.append(strip5)
        
        strip6 = LogoStrip(strip5.get_indexEnd()+1,52)
        self.stripList.append(strip6)
        
        strip7 = LogoStrip(strip6.get_indexEnd()+1,52)
        self.stripList.append(strip7)
        
        strip8 = LogoStrip(strip7.get_indexEnd()+1,52)
        self.stripList.append(strip8)
        
        
        

    def get_border_index(self):
        borderStrip = []
        borderStrip.append(self.stripList[0])
        borderStrip.append(self.stripList[1])
        borderStrip.append(self.stripList[2])
        borderStrip.append(self.stripList[3])
        borderStrip.append(self.stripList[4])
        borderStrip.append(self.stripList[5])
        borderStrip.append(self.stripList[6])
        borderStrip.append(self.stripList[7])
        borderStrip.append(self.stripList[8])
        return self.getIndex(borderStrip)

    def get_border_eyes_mouth_index(self):
        strips = []
        strips.append(self.stripList[0])
        strips.append(self.stripList[1])
        strips.append(self.stripList[2])
        strips.append(self.stripList[3])
        strips.append(self.stripList[4])
        strips.append(self.stripList[5])

        return self.getIndex(strips)
    
    def get_eyes_strips_index(self):
        strips = []
        strips.append(self.stripList[0])
        strips.append(self.stripList[7])
        return self.getIndex(strips)

    def get_bottom_up_border_index(self):
        strips = []
        strips.append(self.getIndex(self.stripList[0]))
        mergedlist = []
        mergedlist.extend(self.getIndex(self.stripList[1]))
        mergedlist.extend(self.getIndex(self.stripList[5]))
        strips.append(mergedlist)
        
        mergedlist = []
        mergedlist.extend(self.getIndex(self.stripList[2]))
        mergedlist.extend(self.getIndex(self.stripList[4]))
        strips.append(mergedlist)
        
        strips.append(self.getIndex(self.stripList[3]))
        return self.getIndex(strips)
    
    def get_bottom_up_border_leds_index(self):
        strips = []
        strips.append(self.getIndex(self.stripList[0]))
        mergedlist = []
        for delta in range (0,51):
            mergedlist.append(self.stripList[0].get_really_indexStart() + delta)
            mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
            mergedlist.append(self.stripList[2].get_really_indexStart() + delta)
            mergedlist.append(self.stripList[3].get_really_indexStart() + delta)
            mergedlist.append(self.stripList[4].get_really_indexStart() + delta)
            mergedlist.append(self.stripList[5].get_really_indexStart() + delta)
            mergedlist.append(self.stripList[6].get_really_indexStart() + delta)
            mergedlist.append(self.stripList[7].get_really_indexStart() + delta)
            strips.append(mergedlist)

        return self.getIndex(strips)
            
    def get_eyes_and_mounth_strips_index(self):
        strips = []
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
        if(type(selectedstripList) == list):
            for logoStrip in  selectedstripList:
                if(type(logoStrip) == LogoStrip) :
                    index =logoStrip.get_indexStart()
                    indexList = []
                    while index <= logoStrip.get_indexEnd():
                        indexs.append(index - 1)
                        index = index+1
                else:
                    indexs.append(logoStrip)
        else:
            index =selectedstripList.get_indexStart()
            indexList = []
            while index <= selectedstripList.get_indexEnd():
                indexList.append(index - 1)
                index = index+1
            return indexList
        return indexs   
        

if __name__ == '__main__':
    logo = LogoFranco();
    
    for count in range(1,11):
        print count
    
    #print "ogo.get_bottom_up_border_leds_index()"
    #print logo.get_bottom_up_border_leds_index()
    

    