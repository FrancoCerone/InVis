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
        delta = 0
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        strips.append(mergedlist)
    
        
        mergedlist = []
        delta = 1
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        strips.append(mergedlist)

        mergedlist = []
        delta = 2
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 3
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 4
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 5
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 6
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        mergedlist.extend(self.getIndex(self.stripList[6]))
        mergedlist.append(self.stripList[7].get_really_indexStart())
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta = 7
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[7].get_really_indexStart()+1)
        
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        
        mergedlist.append(self.stripList[24].get_really_indexEnd())
        mergedlist.append(self.stripList[13].get_really_indexStart())
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 8
        delta_2 = 1
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta_2 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - delta_2)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta_2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 9
        delta_2 = 2
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta_2 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - delta_2)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta_2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 10
        delta_2 = 3
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta_2 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - delta_2)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta_2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 11
        delta_2 = 4
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta_2 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - delta_2)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta_2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 12
        delta_2 = 5
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta_2 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - delta_2)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta_2)
        
        mergedlist.append(self.stripList[15].get_really_indexStart())
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta = 13
        delta_2 = 6
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta_2 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - delta_2)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta_2)
        mergedlist.extend(self.getIndex(self.stripList[11]))
        mergedlist.extend(self.getIndex(self.stripList[12]))
        
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[21].get_really_indexStart())
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 14
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[25].get_really_indexStart() + delta- 14)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd())
        mergedlist.extend(self.getIndex(self.stripList[11]))
        mergedlist.extend(self.getIndex(self.stripList[12]))
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 15
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[25].get_really_indexStart() + delta- 14)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta = 16
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[25].get_really_indexStart() + delta- 14)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 17
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[25].get_really_indexStart() + delta- 14)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 18
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[25].get_really_indexStart() + delta- 14)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 19
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +1)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[25].get_really_indexStart() + delta- 14)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta = 20
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        
        mergedlist.append(self.stripList[26].get_really_indexStart())
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd())
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 21
        
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 22
        
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 23
        
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta = 24
        
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =25
        
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =26
        
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[7].get_really_indexStart()+delta -7 +1)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =27
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =28
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =29
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =30
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        ##duplico le prime 6
        mergedlist = []
        delta =31
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta -1)
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -8))
            
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -21))
        
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 22))
        
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -7)
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 15))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =32
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -7))
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -6))
            
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -19))
        mergedlist.append(self.stripList[26].get_really_indexStart()+ (delta -20))
        
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 13))
        mergedlist.append(self.stripList[10].get_really_indexEnd()- (delta - 14))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[15].get_really_indexStart() + delta- 12)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        #mergedlist.append(self.stripList[1].get_really_indexStart() + delta +2)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =33
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        
        mergedlist.append(self.stripList[24].get_really_indexEnd() - (delta -6))
        
        mergedlist.extend(self.getIndex(self.stripList[27]))
        mergedlist.extend(self.getIndex(self.stripList[28]))
        
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        
        mergedlist.extend(self.getIndex(self.stripList[17]))
        mergedlist.extend(self.getIndex(self.stripList[18]))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta + 1)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =34
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        
        mergedlist.extend(self.getIndex(self.stripList[17]))
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta + 1)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =35
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta + 1)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =36
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        #mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        #mergedlist.append(self.stripList[1].get_really_indexStart() + delta + 1)
        strips.append(mergedlist)
        
                
        mergedlist = []
        delta =37
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-22))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 14)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =38
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-22))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 14)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        strips.append(mergedlist)
        
                
        mergedlist = []
        delta =39
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-22))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 14)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =40
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 20))
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-22))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 14)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =41
        mergedlist.append(self.stripList[5].get_really_indexEnd() - delta - 2)
        
        mergedlist.append(self.stripList[30].get_really_indexEnd() - (delta - 21))
        
        mergedlist.append(self.stripList[13].get_really_indexStart() + delta -6)
        mergedlist.append(self.stripList[14].get_really_indexEnd() - delta - 1)
        
        
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-22))
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-21))
        mergedlist.append(self.stripList[20].get_really_indexEnd()-(delta-20))
        
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 14)
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =42
        mergedlist.extend(self.getIndex(self.stripList[23]))
        mergedlist.extend(self.getIndex(self.stripList[22]))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =43
        mergedlist.append(self.stripList[4].get_really_indexEnd() - (delta - 43))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =44
        mergedlist.append(self.stripList[4].get_really_indexEnd() -(delta - 43))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        
        
        mergedlist = []
        delta =45
        mergedlist.append(self.stripList[4].get_really_indexEnd() - ( delta - 43))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =46
        mergedlist.append(self.stripList[4].get_really_indexEnd()- ( delta - 43))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)

        mergedlist = []
        delta =47
        mergedlist.append(self.stripList[4].get_really_indexEnd() -( delta - 43))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =48
        mergedlist.append(self.stripList[4].get_really_indexEnd() - ( delta - 43))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 13)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        
        mergedlist = []
        delta =49
        mergedlist.append(self.stripList[4].get_really_indexEnd() -(delta - 43))
        mergedlist.append(self.stripList[21].get_really_indexStart()+ delta - 14)
        mergedlist.append(self.stripList[1].get_really_indexStart() + delta+1)
        strips.append(mergedlist)
        mergedlist = []
        
        delta = 50
        strips.append(self.getIndex(self.stripList[3]))

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
    logo = Logo();
    

    
    print "ogo.get_bottom_up_border_leds_index()"
    print logo.get_bottom_up_border_leds_index()
    

    