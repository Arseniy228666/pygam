from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('игра')

bg = transform.scale(image.load('background.png'),(700, 500))

clock=time.Clock()

x1= 100
y1 = 300

x2=300
y2=300

sp = 10



run = True

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()
    g1 = transform.scale(image.load('sprite1.png'),(100, 100))
    g2 = transform.scale(image.load('sprite2.png'),(100, 100))

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= sp
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += sp
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= sp
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += sp 

    if keys_pressed[K_a] and x2 > 5:
        x2 -= sp
    if keys_pressed[K_d] and x2 < 595:
        x2 += sp
    if keys_pressed[K_w] and y2 > 5:
        y2 -= sp
    if keys_pressed[K_s] and y2 < 395:
        y2 += sp 


    window.blit(bg,(0,0))
    window.blit(g1,(x1,y1))
    window.blit(g2,(x2,y2))
    display.update()
    clock.tick(60)