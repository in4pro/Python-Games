import pygame
import time

BACKGROUD_COLOR = (255, 255, 2)
ZERO_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 0, 255)
FIELD_COLOR = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([500, 500])

m = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

def draw_field():
    pygame.draw.line(screen, (FIELD_COLOR), (200, 100), (200, 400), 10) 
    pygame.draw.line(screen, (FIELD_COLOR), (300, 100), (300, 400), 10)
    pygame.draw.line(screen, (FIELD_COLOR), (100, 200), (400, 200), 10)
    pygame.draw.line(screen, (FIELD_COLOR), (100, 300), (400, 300), 10)

def draw_X(x, y):
    pygame.draw.line(screen, (CROSS_COLOR), (x, y), (x + 80, y - 80), 20)
    pygame.draw.line(screen, (CROSS_COLOR), (x, y - 80), (x + 80, y), 20)    

def draw_O(x, y):
    pygame.draw.circle(screen, (ZERO_COLOR), (x, y), 45)
    pygame.draw.circle(screen, (BACKGROUD_COLOR), (x, y), 25)

def mouse_coordinates(pos):
    pos_1 = (pos[0] - 100)//100
    pos_2 = (pos[1] - 100)//100
    if pos[0] < 100 or pos[0] > 400:
        return False
    elif pos[1] < 100 or pos[1] > 400:
        return False
    elif m[pos_2][pos_1] != 0:
        return False
    elif player == 1:
        m[pos_2][pos_1] = 1
        return True
    elif player == -1:
        m[pos_2][pos_1] = -1
        return True
    
def check_line(cnt, val):
    o = True
    for n in range(len(m[cnt])):
        if m[cnt][n] != val:
            o = False
            break
    return o

def check_column(cnt, val):
    o = True
    for n in range(len(m[cnt])):
        if m[n][cnt] != val:
            o = False
            break
    return o

def check_diagonal_1(val):
    o = True
    for n in range(len(m)):
        if m[n][n] != val:
            o = False
            break
    return o

def check_diagonal_2(val):
    o = True
    for n in range(len(m)):
        if m[len(m) - n - 1][n] != val:
            o = False
            break
    return o

def main_check(val):
    for cnt in range(len(m)):
        if check_line(cnt, val):
            return True
    for cnt in range(len(m)):
        if check_column(cnt, val):
            return True
    for cnt in range(len(m)):
        if check_diagonal_1(val):
            return True
    for cnt in range(len(m)):
        if check_diagonal_2(val):
            return True    
    return False
    
running = True
player = 1
while running:
    for event in pygame.event.get():
        draw_field()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            result = mouse_coordinates(pos)
            if not result:
                pass
            else:
                player = player*-1

    screen.fill((BACKGROUD_COLOR))

    draw_field()
    
    for cnt in range(len(m)):
        for n in range(len(m[cnt])):
            if m[cnt][n] == 1:
                draw_X(110 + 100*n, 188 + 100*cnt)
            elif m[cnt][n] == -1:
                draw_O(150 + 100*n, 150 + 100*cnt)
                
    for cnt in range(len(m)):
        for n in range(len(m[cnt])):
            if m[cnt][n] == 0:
                o = True
                break
            else:
                o = False
        if o:
            break
        
    running = o
                
    pygame.display.flip()
    
    if main_check(1):
        time.sleep(3)
        running = False
        
    elif main_check(-1):
        time.sleep(3)
        running = False
    
pygame.quit()
