from pygame import *

def filltool(mx,my):
    get=screen.get_at((mx,my))
    if get==col:      
        screen.set_at((mx,my),(128,128,128))
        filltool(mx+1,my)
        filltool(mx-1,my)
        filltool(mx,my+1)
        filltool(mx,my-1)        
    return
    
penx,peny=0,0
screen=display.set_mode((800,600))
screen.fill((255,255,255))
running=True
while running:
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
        if evnt.type==MOUSEBUTTONDOWN:
            col=screen.get_at((mx,my))        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if mb[0]==1:
        draw.line(screen,(0,0,0),(mx,my),(penx,peny))
    penx,peny=mx,my
    if mb[2]==1:
        filltool(mx,my)
        display.update()
        
    display.flip()
quit()
