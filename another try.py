from pygame import *
from random import *
#init()
#mixer.music.load("song/Yu-Gi-Oh Original Theme song (Full).mp3")
#mixer.music.play()

def pentool():
    #screen.set_clip(canvasRect)
    draw.line(screen,(colour),(ox,oy),(mx,my))
    draw.line(canvas,(colour),(ox-152,oy-100),(mx-152,my-100))

def erasertool():
    #screen.set_clip(canvasRect)
    dx,dy=mx-ox,my-oy
    dist=max(abs(dx),abs(dy))
    for i in range(dist):
        x = int((ox)+float(i)/dist*dx)
        y = int((oy)+float(i)/dist*dy)
        if canvas_erase=="arena":
            eraser=arena.subsurface(int(x-5*thick-152),int(y-5*thick-100),10*thick,10*thick)
        elif canvas_erase=="tablet":
            eraser=tablet.subsurface(int(x-5*thick-152),int(y-5*thick-100),10*thick,10*thick)
        elif canvas_erase=="duel":
            eraser=duel.subsurface(int(x-5*thick-152),int(y-5*thick-100),10*thick,10*thick)
        else:
            eraser=background.subsurface(int(x-5*thick),int(y-5*thick),10*thick,10*thick)
        screen.blit(eraser,(int(x-5*thick),int(y-5*thick)))
        draw.rect(canvas,(255,255,255,0),((int(x-152-5*thick),int(y-100-5*thick),10*thick,10*thick)))



def linetool():
    #screen.set_clip(canvasRect)
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.line(screen,(colour),(startx,starty),(mx,my),thick)

def brushtool():
    #screen.set_clip(canvasRect)
    dx,dy=mx-ox,my-oy
    dist=max(abs(dx),abs(dy))
    for i in range(dist):
        x = int((ox)+float(i)/dist*dx)
        y = int((oy)+float(i)/dist*dy)
        draw.circle(screen,(colour),(x,y),thick)
        draw.circle(canvas,(colour),(x-152,y-100),thick)

def spraytool():
    #screen.set_clip(canvasRect)
    for i in range(20):
        sprx=randint(mx-10-thick*2,mx+10+thick*2)
        spry=randint(my-10-thick*2,my+10+thick*2)
        dist=((mx-sprx)**2+(my-spry)**2)**0.5
        if dist<=10+thick*2:
            draw.circle(screen,(colour),(sprx,spry),0)
            draw.circle(canvas,(colour),(sprx-152,spry-100),0)

def recttool():
    #screen.set_clip(canvasRect)
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.rect(screen,(colour),(startx,starty,mx-startx,my-starty),thick)
    
    
def filledrect():
   # screen.set_clip(canvasRect)
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.rect(screen,(colour),(startx,starty,mx-startx,my-starty))
        
def ellipsetool():
   # screen.set_clip(canvasRect)
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        if abs(mx-startx)>thick*2 and abs(my-starty)>thick*2:
            draw.ellipse(screen,(colour),(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),thick)
        else:
            draw.ellipse(screen,(colour),(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)))
        
def filledellipse():
    #screen.set_clip(canvasRect)
    if mb[0]==1:
        screen.set_clip(canvasRect)
        screen.blit(newscreen,(0,0))
        draw.ellipse(screen,(colour),(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)))
        
def eyedroppertool():
    global colour
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        colour=screen.get_at((mx-152,my-100))
    

def filltool(mx, my):
    #screen.set_clip(canvasRect)
    pixCol=canvas.get_at((mx-152,my-100))
    if pixCol==colour:
        return
    edge=[(mx-152,my-100)]
    canvas.set_at((mx-152, my-100), (colour))
    for (mx, my) in edge:
        for (x, y) in ((mx+1, my), (mx-1, my), (mx, my+1), (mx, my-1)):
            if 0<mx<719 and 0<my<479:
                if canvas.get_at((x, y))==pixCol:
                    canvas.set_at((x, y), (colour))                    
                    edge.append((x, y))
    screen.blit(canvas,(152,100))

def cleartool():    
    if canvas_erase=="arena":
        clear=arena.subsurface(0,0,720,480)
    elif canvas_erase=="tablet":
        clear=tablet.subsurface(0,0,720,480)
    elif canvas_erase=="duel":
        clear=duel.subsurface(0,0,720,480)
    else:
        clear=background.subsurface(152,100,720,480)
    screen.blit(clear,(152,100))
    draw.rect(canvas,(255,255,255,0),(0,0,720,480))

#===========================================================================#
selectRect=Rect(0,0,0,0)
selected=0,0,0,0
sx,sy=0,0
newrect=Rect(0,0,0,0)
subRect=Rect(0,0,0,0)

def selecttool():
    global selectRect, selected, sx, sy,newrect,subRect
    #layer.set_clip((20,20,836,653))
    if mb[0] == 1:
        screen.blit(newscreen,(0,0))
        newrect=Rect(startx-152,starty-100,mx-startx,my-starty)
        selectRect = draw.rect(screen,(128,128,128),(startx,starty,mx-startx,my-starty),1)
        selected = canvas.subsurface(min(mx,startx)-152,min(my,starty)-100,abs(mx-startx),abs(my-starty)).copy()
        sx,sy = selected.get_size()        
        if canvas_erase=="arena":
            subRect=arena.subsurface(newrect)
        elif canvas_erase=="tablet":
            subRect=tablet.subsurface(newrect)
        elif canvas_erase=="duel":
            subRect=duel.subsurface(newrect)
        else:            
            subRect=background.subsurface(selectRect)
        
    elif mb[2] == 1 and selectRect.collidepoint((startx,starty)):
        screen.blit(newscreen,(0,0))
        screen.blit(subRect,selectRect)
        draw.rect(canvas,(255,255,255,0),newrect)
        screen.blit(selected,(mx-sx//2,my-sy//2))
        
   # if evnt.type == MOUSEBUTTONUP:
    #    if evnt.button == 3:
     #       canvas.blit(selected,(mx-sx//2-152,my-sy//2-100))

#===========================================================================#
    


#keys=""
#def texttool():
 #   keys=key.get_pressed()   
    

tool=""        
                
            
screen=display.set_mode((1024,768))
background=image.load("NewBack5.png")
screen.blit(background,(0,0,1024,768))

colRect=Rect(887,638,124,90)

#============================CANVAS BG========================================#

arena=image.load("images/Duel Arena.png")
tablet=image.load("images/Millenium Tablet.png")
duel=image.load("images/Final Duel.png")

canvasBG="canvas"

canvasNames=[arena,tablet,duel]

canvas_erase=""

canvas_names=["arena","tablet","duel"]

canvas_Rect=[]

def canvas_BG():
    for i in range(len(canvasNames)):
        scale_canvas=transform.scale(canvasNames[i],(180,120))
        screen.blit(scale_canvas,(185+i*240,620))
        scale_rect=draw.rect(screen,(128,128,128),(185+i*240,620,180,120),3)
        canvas_Rect.append(scale_rect)

def blitCanvas():
    global canvas_erase
    for i in range(len(canvasNames)):
        if mb[0]==1 and canvas_Rect[i].collidepoint((mx,my)):
            screen.blit(canvasNames[i],(152,100))
            canvas_erase=canvas_names[i]
    screen.blit(canvas,(152,100))        
    
#===========================TOOL STUFF========================================#
#loads all tool and stamp pictures
#enters loaded surfaces into a dictionary
def loadPics(list1,list2):
    global allPics
    for pic in list1:
        allPics[pic]=image.load("images/"+pic+"S.png")
    #for pic in list1:                  #clear, save, load, undo and redo do not have selected picture
        allPics["sel"+pic]=image.load("images/"+pic+".png")
    for pic in list2:
        #allPics[pic]=image.load("images/M"+pic+".png")
        allPics[pic+"BW"]=image.load("images/"+pic+"BW.png")
        allPics["sel"+pic]=image.load("images/"+pic+".png")
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
#    if evnt.type==KEYDOWN:
 #       if evnt.key == K_LEFT:
  #          turn += 20
   #     elif evnt.key == K_RIGHT:
    #        turn -= 20
     #   if evnt.key == K_UP:
      #      size += 0.1   
       # elif evnt.key == K_DOWN:
        #    if size>0.2:
         #       size -= 0.1
    for i in range(len(stampList)):
        if tool==stampList[i]:
            stamp_image=image.load("images/N"+stampList[i]+".png")
            changedstamp = transform.rotozoom(stamp_image, turn, size)
            stampw, stamph = changedstamp.get_width(), changedstamp.get_height()
    if mb[0]==1:
        screen.blit(newscreen,(0,0))
        screen.blit(changedstamp,(mx-stampw//2,my-stamph//2))
    #if evnt.type == MOUSEBUTTONUP:
        #if evnt.button==1:
            #canvas.blit(changedstamp,(mx-stampw//2-152,my-stamph//2-100))



allPics={}                                  #dictionary for loaded surfaces
toolList=["pencil","line","spray","fill","rect","ellipse","polygon","eraser",
          "brush","eyedropper","text","filledrect","filledellipse","select"]
stampList=["puzzle","eye","ring","scale","key","rod","necklace","pyramid"]



toolRects=[]
for i in range(14):
    if i<7:
        t_rects=Rect(35,350+i*37,32,32)
    else:
        t_rects=Rect(87,350+(i-7)*37,32,32)
    toolRects.append(t_rects)


stampRects=[]
for i in range(8):
    s_rects=Rect(162+i*90,20,80,60)
    stampRects.append(s_rects)

loadPics(toolList,stampList)                #loads all pictures
blitTools(toolList,toolRects)               #blits tools
blitStamps(stampList,stampRects)            #blits stamps


#allows only one tool to be highlighted at a time
allToolRect=Rect(35,350,92,291)
allToolPic=screen.subsurface(allToolRect).copy()
tools()
allToolPic=screen.subsurface(allToolRect).copy()

#allows only one stamp to be highlighted at a time
allStampRect=Rect(162,20,710,60)
allStampPic=screen.subsurface(allStampRect).copy()
stamps()
allStampPic=screen.subsurface(allStampRect).copy()


canvasRect=Rect(152,100,720,480)

canvas=Surface((720,480),SRCALPHA)
canvas.fill((255,255,255,0))

#============================UNDO REDO STUFF======================================#
undorect=draw.rect(screen,(255,255,255),(900,500,25,25))
redorect=draw.rect(screen,(255,255,255),(900,550,25,25))

undolist=[canvas.copy()]
redolist=[]
undopos=0

#=============================================================================#



colour=(0,0,0)
thick=1
mx,my=0,0
running = True
first=True
while running:  
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

        
           
       
            if undorect.collidepoint(mx,my) and undopos>0:
                undopos-=1
                cleartool()
                canvas.blit(undolist[undopos],(0,0))
            if redorect.collidepoint((mx,my)) and undopos<len(undolist)-1:
                undopos+=1
                canvas.blit(undolist[undopos],(0,0))
                    

        if evnt.type==MOUSEBUTTONUP:
            if undopos<len(undolist)-1:
                del undolist[undopos+1::]
            if canvasRect.collidepoint(mx,my) and tool!="" and tool!="eyedropper":    
                undolist += [canvas.copy()]
                undopos+=1
            if evnt.button==1:# and canvasRect.collidepoint(mx,my):
                if tool=="line":
                    draw.line(canvas,(colour),(startx-152,starty-100),(mx-152,my-100),thick)
                elif tool=="rect":
                    draw.rect(canvas,(colour),(startx-152,starty-100,mx-startx,my-starty),thick)
                elif tool=="filledrect":
                    draw.rect(canvas,(colour),(startx-152,starty-100,mx-startx,my-starty))
                elif tool=="ellipse":
                    if abs(mx-startx)>thick*2 and abs(my-starty)>thick*2:
                        draw.ellipse(canvas,(colour),(min(mx,startx)-152,min(my,starty)-100,abs(mx-startx),abs(my-starty)),thick)
                    else:
                        draw.ellipse(canvas,(colour),(min(mx,startx)-152,min(my,starty)-100,abs(mx-startx),abs(my-starty)))
                elif tool=="filledellipse":
                    draw.ellipse(canvas,(colour),(min(mx,startx)-152,min(my,starty)-100,abs(mx-startx),abs(my-starty)))
                #for i in range(len(stampList)):
                 #   if tool==stampList[i]:
                  #      canvas.blit(changedstamp,(mx-stampw//2-152,my-stamph//2-100))
                        
            elif evnt.button==3:
                if tool=="select":
                    canvas.blit(selected,(mx-sx//2-152,my-sy//2-100))
                
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

    #if mb[0]==1 and stampArea.collidepoint((mx,my)):
        #screen.set_clip()
        #selStamps()
   # texttool()
    
    if canvasBG=="canvas":
        canvas_BG()
    blitCanvas()
    #if mb[0]==1 and toolArea.collidepoint((mx,my)):
       # screen.set_clip()
        #toolBox()
    tools()
    stamps()

    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        for i in range(len(stampList)):
            if tool==stampList[i]:
                stamps_blit()
        if tool=="select":
            selecttool()
        screen.set_clip(0,0,1024,768)   
        
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
    

    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        if tool=="fill":
            filltool(mx,my)
        
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
        

        screen.set_clip(0,0,1024,768)      
    #if tool=="clear":
        #cleartool()
    #if mb[0]==1:
       # print(mx,my)
    #if canvasRect.collidepoint(mx,my) :
     #   print(canvas.get_at((mx-152,my-100)))
    #print(canvas_erase)
    print(len(redolist),"\n",len(undolist))
    
    

    display.flip()
quit()

