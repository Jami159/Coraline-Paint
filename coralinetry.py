from pygame import *
from random import *
from text import*
from glob import *
init()
font.init()



#============================TEXT TOOL=======================================#

comicFont = font.SysFont("Times New Roman", 20)
def getname(screen,showFiles):
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 20)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(startx,starty,mx-startx,my-starty) # make changes here.

    if showFiles:
        pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
        n = len(pics)
        choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
        for i in range(n):
            txtPic = arialFont.render(pics[i], True, (0,111,0))   #
            screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
        
    typing = True
    while typing:
        for evnt in event.get():
            if evnt.type == QUIT:
                event.post(evnt)   # puts QUIT back in event list so main quits
                return ""
            if evnt.type == KEYDOWN:
                if evnt.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        clear=background.subsurface(startx,starty,len(ans)*15,25)
                        screen.blit(clear,(startx,starty))
                        draw.rect(canvas,(255,255,255,0),(startx,starty,len(ans)*15,25))
                        ans = ans[:-1]
                elif evnt.key == K_KP_ENTER or evnt.key == K_RETURN : 
                    typing = False
                elif evnt.key < 256:
                    ans += evnt.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (colour))   #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans

#stole sir's getname function

#============================================================================#


#draws a line at every point the mouse passes through to create a pencil effect
def pentool():
    draw.line(screen,(colour),(ox,oy),(mx,my))
    draw.line(canvas,(colour),(ox-250,oy-150),(mx-250,my-150))


#subsurfaces the background to make it appear as though the drawings are being
#erased, draws a clear rectangle to patch up the canvas after the background has
#been subsurfaced
def erasertool():
    dx,dy=mx-ox,my-oy                       
    dist=max(abs(dx),abs(dy))               
    for i in range(dist):                   
        x = int((ox)+float(i)/dist*dx)
        y = int((oy)+float(i)/dist*dy)
        if 250<x<1050 and 150<y<750:        
            eraser=background.subsurface(int(x-5*thick),int(y-5*thick),10*thick,10*thick)
            screen.blit(eraser,(int(x-5*thick),int(y-5*thick)))
            draw.rect(canvas,(255,255,255,0),((int(x-250-5*thick),int(y-150-5*thick),10*thick,10*thick)))


#draws a staright line from where the user has clicked to where he has released
def linetool():
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.line(screen,(colour),(startx,starty),(mx,my),thick)


#uses similar triangles to find the integer intervals between #two points,
#and draws circles at every interval to create a brush effect
def brushtool():
    dx,dy=mx-ox,my-oy
    dist=max(abs(dx),abs(dy))
    for i in range(dist):
        x = int((ox)+float(i)/dist*dx)
        y = int((oy)+float(i)/dist*dy)
        draw.circle(screen,(colour),(x,y),thick)
        draw.circle(canvas,(colour),(x-250,y-150),thick)


#draws random circles within a certain radius to create a spray paint effect
def spraytool():
    for i in range(20):
        sprx=randint(mx-10-thick*2,mx+10+thick*2)
        spry=randint(my-10-thick*2,my+10+thick*2)
        dist=((mx-sprx)**2+(my-spry)**2)**0.5
        if dist<=10+thick*2:
            draw.circle(screen,(colour),(sprx,spry),0)
            draw.circle(canvas,(colour),(sprx-250,spry-150),0)


#draws a rectangle from where the user has clicked to where he has released
def recttool():
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.rect(screen,(colour),(startx,starty,mx-startx,my-starty),thick)
        
def filledrect():
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.rect(screen,(colour),(startx,starty,mx-startx,my-starty))


#draws an ellipse from where the user has clicked to where he has released        
def ellipsetool():
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        if abs(mx-startx)>thick*2 and abs(my-starty)>thick*2:
            draw.ellipse(screen,(colour),(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),thick)
        else:
            draw.ellipse(screen,(colour),(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)))
       
def filledellipse():
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.ellipse(screen,(colour),(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)))

#takes the colour value from the canvas        
def eyedroppertool():
    global colour
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        colour=canvas.get_at((mx-250,my-150))
    

#fills with colour within a boundary
def filltool(mx, my):
    pixCol=canvas.get_at((mx-250,my-150))
    if pixCol==colour: 
        return
    edge=[(mx-250,my-150)]
    canvas.set_at((mx-250, my-150), (colour))
    for (mx, my) in edge:
        for (x, y) in ((mx+1, my), (mx-1, my), (mx, my+1), (mx, my-1)):
            if 0<mx<799 and 0<my<599:
                if canvas.get_at((x, y))==pixCol:
                    canvas.set_at((x, y), (colour))                    
                    edge.append((x, y))
    screen.blit(canvas,(250,150))


def cleartool():    
    clear=background.subsurface(250,150,800,600)
    screen.blit(clear,(250,150))
    draw.rect(canvas,(255,255,255,0),(0,0,800,600))

clearRect=Rect(122,390,85,30)


#===============================MUSIC STUFF==================================#
#def playMusic():
 #   global musicOn
 #   if musicOn == True:
 #       musicOn = False
 #   else:
 #       musicOn = True
        
 #   if musicOn == False:
 #       mixer.music.pause()
 #       screen.blit(image.load("Image/musicOff.png"),(175,585))                               
 #   elif musicOn == True:
 #       mixer.music.unpause()
 #       screen.blit(image.load("Image/musicOn.png"),(175,585))  


#music = Rect(175,585,32,32)
#musicOn = True
#song = mixer.music.load("song/Coraline  Soundtrack Song- Exploration.mp3")
#mixer.music.pause()

 
#===========================================================================#
selectRect=Rect(0,0,0,0)
selected=0,0,0,0
sx,sy=0,0
newrect=Rect(0,0,0,0)
subRect=Rect(0,0,0,0)

def selecttool():
    global selectRect, selected, sx, sy,newrect,subRect
    if mb[0] == 1:
        screen.blit(newscreen,(0,0))
        newrect=Rect(startx-250,starty-150,mx-startx,my-starty)
        selectRect = draw.rect(screen,(128,128,128),(startx,starty,mx-startx,my-starty),1)
        selected = canvas.subsurface(min(mx,startx)-250,min(my,starty)-150,abs(mx-startx),abs(my-starty)).copy()
        sx,sy = selected.get_size()           
        subRect=background.subsurface(selectRect)
        
    elif mb[2] == 1 and selectRect.collidepoint((startx,starty)):
        screen.blit(newscreen,(0,0))
        screen.blit(subRect,selectRect)
        draw.rect(canvas,(255,255,255,0),newrect)
        screen.blit(selected,(mx-sx//2,my-sy//2))
        
#===========================================================================#
def polygontool():
    global a,b
    if mb[0] == 1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        if firstpoint == False:
            draw.line(screen,colour,(startx,starty),(mx,my),thick)
        elif firstpoint == True:
            draw.line(screen,colour,(nx,ny),(mx,my),thick)  
    

tool=""        
                
            
screen=display.set_mode((1280,800))

colRect=Rect(41,631,164,109)


#============================CANVAS BG========================================#

BG1=draw.rect(screen,(255,255,255),(40,590,30,30))
BG2=draw.rect(screen,(255,255,255),(90,590,30,30))
BG3=draw.rect(screen,(255,255,255),(140,590,30,30))

coraline = image.load("coraline.png")
careful = image.load("careful.png")
night = image.load("night.png")

bgpic = [coraline,careful,night]
    
theme = 1
changeTheme = Rect(18,700,62,63)
background = coraline

screen.blit(background,(0,0))
screen.blit(image.load("Image/empty.png"),(30,165))

def canvasSelect():
    global background
    if mb[0]==1:
        if BG1.collidepoint(mx,my):
            background=coraline
            
        elif BG2.collidepoint(mx,my):
            background=careful
            
        elif BG3.collidepoint(mx,my):
            background=night

    screen.blit(background,(0,0))
    draw.rect(screen,(128,128,128),(40,590,30,30))
    draw.rect(screen,(128,128,128),(85,590,30,30))
    draw.rect(screen,(128,128,128),(130,590,30,30))
    screen.blit(image.load("Image/empty.png"),(30,165))
    screen.blit(canvas,(250,150))


def colourShow():
    if background==coraline:
        draw.rect(screen,(colour),(40,590,30,30))
    elif background==careful:
        draw.rect(screen,(colour),(85,590,30,30))
    elif background==night:
        draw.rect(screen,(colour),(130,590,30,30))




#===========================TOOL AND STAMP STUFF========================================#
#loads all tool and stamp pictures
#enters loaded surfaces into a dictionary
def loadPics(list1,list2):
    global allPics
    for pic in list1:
        allPics[pic]=image.load("Image/blank.png")
    for pic in list1:                  #clear, save, load, undo and redo do not have selected picture
        allPics["sel"+pic]=image.load("Image/border.png")
    for pic in list2:
        #allPics[pic]=image.load("images/M"+pic+".png")
        allPics[pic+"BW"]=image.load("Image/"+pic+"BW.png")
        allPics["sel"+pic]=image.load("Image/"+pic+".png")
#blits tools onto screen
def blitTools(list1,list2):
    for i in range(len(list1)):
        screen.blit(allPics[list1[i]],list2[i])

#blits stamp thumbnails onto screen
def blitStamps(list1,list2):
    for i in range(len(list1)):
        screen.blit(allPics[list1[i]+"BW"],list2[i])

#selects a tool or stamp when the mouse clicks on its icon
#save, load, and clear cannot become the selected tool or they will loop
def toolselecter(name,rect):
    global tool
    mpos=mouse.get_pos()
    mb=mouse.get_pressed()
    if rect.collidepoint(mpos) and mb[0]==1:
        tool=name

#checks which tool is selected
#blits a highlighted picture of the selected tool
#undo and redo are not a part of this function
def tools():
    global tool
    screen.blit(allToolPic,allToolRect)     #allows only one tool to be highlighted at a time
    
    for i in range(len(toolList)):
        toolselecter(toolList[i],toolRects[i])
        if tool==toolList[i]:
            screen.blit(allPics["sel"+toolList[i]],toolRects[i])

#checks which stamp is selected
#blits a highlighted picture of the selected stamp
def stamps():
    global tool
    screen.blit(allStampPic,allStampRect)   #allows only one stamp to be hightlighted at a time
    
    for i in range(len(stampList)):
        toolselecter(stampList[i],stampRects[i])
        if tool==stampList[i]:
            screen.blit(allPics["sel"+stampList[i]],stampRects[i])


size=1
turn=0
stampw,stamph=0,0
def stamps_blit():
    #global size, turn, stampw, stamph
    screen.set_clip((canvasRect))    
    for i in range(len(stampList)):
        if tool==stampList[i]:
            stamp_image=image.load("Image/M"+stampList[i]+".png")
            changedstamp = transform.rotozoom(stamp_image, turn, size)
            stampw, stamph = changedstamp.get_width(), changedstamp.get_height()
    if mb[0]==1:
        screen.blit(newscreen,(0,0))
        screen.blit(changedstamp,(mx-stampw//2,my-stamph//2))
    

allPics={}                                  #dictionary for loaded surfaces
toolList=["pencil","eraser","line","brush","spray","eyedropper","fill","text",
          "rect","filledrect","ellipse","filledellipse","polygon","select"]
stampList=["coraline","cat","mom","doll","bob","miss"]



toolRects=[]
for i in range(14):
    if i<4:
        t_rects=Rect(28+i*47,248,32,32)
    elif i<8:
        t_rects=Rect(28+(i-4)*47,295,32,32)
    elif i<12:
        t_rects=Rect(28+(i-8)*47,342,32,32)
    else:
        t_rects=Rect(28+(i-12)*47,389,32,32)
    toolRects.append(t_rects)


stampRects=[]
for i in range(6):
    s_rects=Rect(1090,200+i*90,150,75)
    stampRects.append(s_rects)

loadPics(toolList,stampList)                #loads all pictures
blitTools(toolList,toolRects)               #blits tools
blitStamps(stampList,stampRects)            #blits stamps


#allows only one tool to be highlighted at a time
allToolRect=Rect(28,248,178,178)
allToolPic=screen.subsurface(allToolRect).copy()
tools()
allToolPic=screen.subsurface(allToolRect).copy()

#allows only one stamp to be highlighted at a time
allStampRect=Rect(1090,200,150,525)
allStampPic=screen.subsurface(allStampRect).copy()
stamps()
allStampPic=screen.subsurface(allStampRect).copy()

#=============================================================================#
wordpics=[]
for i in range(len(toolList)):
    word_image=image.load("Image/"+toolList[i]+".png")
    wordpics.append(word_image)

def descriptions():
    for i in range(len(toolList)):
        if tool==toolList[i]:
            screen.blit(wordpics[i],(30,165))
    for i in range(len(stampList)):
        if tool==stampList[i]:
            screen.blit(image.load("Image/stamps.png"),(30,165))
            


canvasRect=Rect(250,150,800,600)

canvas=Surface((800,600),SRCALPHA)
canvas.fill((255,255,255,0))

#============================UNDO REDO STUFF==================================#
undorect=Rect(123,437,33,32)
redorect=Rect(169,437,33,32)

undolist=[canvas.copy()]
redolist=[] 

first=True      
#=============================SAVE AND LOAD===================================#

saverect=Rect(32,437,32,32)

loadrect=Rect(76,437,32,32)

yesrect=Rect(56,561,50,20)
norect=Rect(127,561,50,20)

saveload=False
yes=False
#=============================================================================#

closed=False            #for polygontool
firstpoint=False        #for polygontool


colour=(0,0,0)
thick=1
mx,my=0,0
startx,starty=0,0
running = True

while running:
    
    for i in range(len(stampList)):
        if tool==stampList[i]:
            stamp_image=image.load("Image/M"+stampList[i]+".png")
            changedstamp = transform.rotozoom(stamp_image, turn, size)
            stampw, stamph = changedstamp.get_width(), changedstamp.get_height()
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
        if evnt.type==MOUSEBUTTONDOWN:
            if evnt.button==4:
                if thick!=10:
                    thick+=1
            elif evnt.button==5:
                if thick>1:
                    thick-=1
                   
            startx,starty=mouse.get_pos()
            newscreen=screen.copy()
            canvascreen=canvas.copy()

            if canvasRect.collidepoint(mx,my) and evnt.button==1 and tool!="" and tool!="eyedropper":
               undolist.append(canvas.copy())
               first=True
               redolist=[]
            if undorect.collidepoint(mx,my) and evnt.button==1:
                if first:
                    redolist.append(canvas.copy())
                    first=False
                if len(undolist)>1:
                    cleartool()                    
                    canvas.blit(undolist[-1],(0,0))
                    redolist.append(undolist[-1])
                    undolist.pop()
                    
            elif redorect.collidepoint(mx,my) and evnt.button==1:
                if len(redolist)>1:
                    cleartool()
                    canvas.blit(redolist[-2],(0,0))
                    undolist.append(redolist[-1])
                    redolist.pop()

            #if music.collidepoint(mx,my):
             #   playMusic()

            if clearRect.collidepoint(mx,my):
                cleartool()
                    
        if evnt.type==MOUSEBUTTONUP:
            if undorect.collidepoint(mx,my) and evnt.button==1:
                screen.blit(background.subsurface(canvasRect),(250,150))
                screen.blit(canvas,(250,150))
               
            if evnt.button==1 and canvasRect.collidepoint(startx,starty):
                if tool=="line":
                    draw.line(canvas,(colour),(startx-250,starty-150),(mx-250,my-150),thick)
                elif tool=="rect":
                    draw.rect(canvas,(colour),(startx-250,starty-150,mx-startx,my-starty),thick)
                elif tool=="filledrect":
                    draw.rect(canvas,(colour),(startx-250,starty-150,mx-startx,my-starty))
                elif tool=="ellipse":
                    if abs(mx-startx)>thick*2 and abs(my-starty)>thick*2:
                        draw.ellipse(canvas,(colour),(min(mx,startx)-250,min(my,starty)-150,abs(mx-startx),abs(my-starty)),thick)
                    else:
                        draw.ellipse(canvas,(colour),(min(mx,startx)-250,min(my,starty)-150,abs(mx-startx),abs(my-starty)))
                elif tool=="filledellipse":
                    draw.ellipse(canvas,(colour),(min(mx,startx)-250,min(my,starty)-150,abs(mx-startx),abs(my-starty)))
                
                elif tool == "polygon":
                    if canvasRect.collidepoint((startx,starty)):                        
                        if firstpoint == False:
                            draw.line(canvas,colour,(startx-250,starty-150),(mx-250,my-150),thick)
                            a,b = startx,starty
                        elif firstpoint == True:
                            draw.line(canvas,colour,(nx-250,ny-150),(mx-250,my-150),thick)
                        nx,ny = mx,my
                        closed = False
                        firstpoint = True
                if canvasRect.collidepoint(mx,my):
                    for i in range(len(stampList)):
                        if tool==stampList[i]:
                            canvas.blit(changedstamp,(mx-stampw//2-250,my-stamph//2-150))
                             
            elif evnt.button==3:
                if tool=="select":
                    canvas.blit(selected,(mx-sx//2-250,my-sy//2-150))
                elif tool=="polygon":
                    if closed == False:
                        draw.line(canvas,colour,(a-250,b-150),(nx-250,ny-150),thick)
                    closed = True
                    firstpoint = False
                    
    
    if evnt.type==KEYDOWN:
        if evnt.key == K_LEFT:
            turn += 20
        elif evnt.key == K_RIGHT:
            turn -= 20
        if evnt.key == K_UP:
            size += 0.1   
        elif evnt.key == K_DOWN:
            if size>0.2:
                size -= 0.1
                
           
    ox,oy=mx,my
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if mb[0]==1 and colRect.collidepoint(mx,my):
        colour=screen.get_at((mx,my))

        
    #canvasSelect()    
    #colourShow()
    
    tools()
    stamps()
    descriptions()
    

    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        for i in range(len(stampList)):
            if tool==stampList[i]:
                stamps_blit()
        if tool=="select":
            selecttool()
        screen.set_clip(0,0,1280,800)
        
    if canvasRect.collidepoint(startx,starty):        
        if tool=="line":
            linetool()
        elif tool=="rect":
            recttool()
        elif tool=="filledrect":
            filledrect()
        elif tool=="ellipse":
            ellipsetool()
        elif tool=="filledellipse":
            filledellipse()
        elif tool=="polygon":
            polygontool()
    

    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        if tool=="fill":
            filltool(mx,my)
        elif tool=="text":
            txt = getname(screen,False)                     # this is how you would call my getName function
                                            # your main loop will stop looping until user hits enter
            txtPic = comicFont.render(txt, True, (colour))
            canvas.blit(txtPic,(mx-250,my-150))
        
    if  mb[0]==1:
        screen.set_clip(canvasRect)
        if tool=="pencil":
            pentool()
        elif tool=="spray":
            spraytool()       
        elif tool=="brush":
            brushtool()        
        elif tool=="eraser":
            erasertool()
        elif tool=="eyedropper":
            eyedroppertool()
        

        screen.set_clip(0,0,1280,800)      
    
        
    if mb[0]==1:
        print(mx,my)
   
    if saverect.collidepoint(mx,my) and mb[0]==1:# tool=="Save":
        txt = getName(screen,False)
        if "." not in txt:
            txt+=".jpg"
        screen_image=canvas.copy()                   
        image.save(screen_image.subsurface(0,0,800,600),(txt))# Saves all the images in a seprate folder
        tool="pencil"
    if loadrect.collidepoint(mx,my) and mb[0]==1:# tool=="Load":
        try:
            txt = getName(screen,False)
            if "." not in txt:
                txt+=".jpg"
            loadimage=image.load(txt)           
            canvas.blit(loadimage,(0,0))
            tool="pencil"
        except:""
    
    
      

            
    text = font.Font(None, 20)
    postext = text.render("(mx,my):  ("+str(mx-250)+", "+str(my-150)+")", 10, (0,0,0))
    draw.rect(screen,(255,255,255),(40,117,140,15))
    screen.blit(postext,(40,117,75,15))
    sizetext = text.render("size:  "+str(thick),10,(0,0,0))
    draw.rect(screen,(255,255,255),(40,140,140,15))
    screen.blit(sizetext,(40,140,75,15))
    #screen.blit(image.load("Image/SaveLoad.png"),(27,525))   
    screen.blit(canvas,(250,150))

    display.flip()
font.quit()
del comicFont
quit()

