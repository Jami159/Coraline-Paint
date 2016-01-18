from pygame import *

def fill(mx,my):
    get=screen.get_at((mx,my))
    if get==(0,0,0):
        return
    edge=[(mx,my)]
    #screen.set_at((mx, my), (0,0,0))
    for (mx, my) in edge:
        for (x, y) in ((mx+1, my), (mx-1, my), (mx, my+1), (mx, my-1)):
            if screen.get_at((x, y))==get:
                screen.set_at((x, y), (0,0,0))
                edge.append((x, y))

def selecttool():
    global selectRect, selected, sx, sy
    layer.set_clip((20,20,836,653))
    if mb[0] == 1:
        layer.blit(newscreen,(0,0)) 
        selectRect = Rect(x,y,mx-x,my-y)
        selected = layer.subsurface(selectRect).copy()
        sx,sy = selected.get_size()
    elif mb[2] == 1 and selectRect.collidepoint((x,y)):
        layer.blit(newscreen,(0,0)) 
        layer.blit(cathat.subsurface(selectRect),selectRect)
        layer.blit(selected,(mx-sx//2,my-sy//2))

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
    draw.rect(screen,(0,0,0),(1,1,798,598),1)
    if mb[0]==1:
        draw.line(screen,(0,0,0),(mx,my),(penx,peny))
    penx,peny=mx,my
    if mb[2]==1:
        fill(mx,my)
        
    display.flip()
quit()
