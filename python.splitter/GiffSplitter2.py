from PIL import Image
import zipfile
import os

os.chdir('.')

def analyseImage(path):
    '''
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode 
    before processing all frames.
    '''
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results






def processImage(path, imageName):
    '''
    Iterate the GIF, extracting each frame.
    '''
    mode = analyseImage(path)['mode']
    
    frameCounter = get_FrameNumbers(path)
    
    im = Image.open(path)
    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')
    try:
        while True:
            if not im.getpalette():
                im.putpalette(p)
            
            new_frame = Image.new('RGBA', im.size)
            if mode == 'partial':
                new_frame.paste(last_frame)
            
            new_frame.paste(im, (0,0), im.convert('RGBA'))
            if(i<10):
                prefix='0'
            else:
                prefix=''
            print im
            if(i==0):
                commanderFolder = get_commanderFolder(os)
                new_frame.save(commanderFolder+imageName + '.png', 'PNG')
                animationFolder = get_AnimationFolder(os)
                new_frame.save(animationFolder+imageName + '.png', 'PNG')
                jpgFolder = get_JpgFolder(os)
                new_frame.save(jpgFolder+imageName + '.png', 'PNG')
                outZipFolder=  get_ZipFolder(os)+ imageName
                os.makedirs(outZipFolder)
            if(i == frameCounter/3):
                new_frame.save(jpgFolder+imageName + '2.png', 'PNG')
                print "secondaimmagine ", i
            if (i == frameCounter*2/3):
                new_frame.save(jpgFolder+imageName + '3.png', 'PNG')
                print 'terzaimmagine ', i 
            
            new_frame.save(outZipFolder +"/" + prefix+'%d.png' % ( i), 'PNG')

            if (i +1 == frameCounter):
                new_frame.save(jpgFolder+imageName + '4.png', 'PNG')
                print 'ultimaimmagine ', i
                zf = zipfile.ZipFile(outZipFolder + ".zip", "w")
                for dirname, subdirs, files in os.walk(outZipFolder):
                    #zf.write(dirname)
                    for filename in files:
                        zf.write(os.path.join(dirname, filename),filename)
                zf.close()
            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass


def main():
   
    #processImage('/home/franco/Desktop/franco1.gif', 'franco1')
    #processImage('/home/franco/Desktop/franco2.gif', 'franco2')
    #processImage('/home/franco/Desktop/franco3.gif', 'franco3')
    #processImage('/home/franco/Desktop/franco4.gif', 'franco4')
    
    print "Done!"

 
def get_JpgFolder(os):
    os.chdir('.')
    jpgFolder = os.path.abspath(os.curdir) + '/python.dialog/resources/pngs/'
    print 'Png folder: ' + jpgFolder
    return jpgFolder   

def get_commanderFolder(os):
    os.chdir('..')
    commanderFolder = os.path.abspath(os.curdir) + '/python.android/resources/'
    print 'commander Folder: ' + commanderFolder
    return commanderFolder 

def get_AnimationFolder(os):
    os.chdir('.')
    animationFolder = os.path.abspath(os.curdir) + '/python.dialog/resources/animations/'
    print 'Animation folder: ' + animationFolder
    return animationFolder
def get_ZipFolder(os):
    os.chdir('.')
    animationFolder = os.path.abspath(os.curdir) + '/python.dialog/resources/zips/'
    print 'Animation folder: ' + animationFolder
    return animationFolder

def get_FrameNumbers(path):
    imToCount = Image.open(path)
    frameCounter = 1;
    try:
        while True:
            imToCount.seek(imToCount.tell() + 1)
            frameCounter =frameCounter +  1
    except EOFError:
        pass
    print 'Dimensione immsgini gif', frameCounter
    return frameCounter
    

if __name__ == "__main__":
    main()