import pygame
import math
from datetime import datetime



pygame.init()
screen = pygame.display.set_mode((980, 700))
screen.fill((255, 255, 255))

# test, position, radius og navn på uret
pygame.display.set_caption("Analog ur")
black = (0, 0, 0)
red = (150, 0, 0)
start_position = (980//2, 700//2)
radius = 200

# starten af while loop
while True:
    screen.fill((255, 255, 255))
# visere der er opdelt i sekunder, minuter og timer

# sekunder
    angle = 360/60*datetime.now().second - 90
    end_offset = [radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (red), start_position, end_position, 2)

# minute
    angle = 360/60*datetime.now().minute - 90
    end_offset = [radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (black), start_position, end_position, 3)

# timer
    angle = 360/12*datetime.now().hour - 90
    end_offset = [radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1] + end_offset[1])
    pygame.draw.line(screen, (black), start_position, end_position, 5)
    
# For loop der viser tal rundt på uret
    for i in range(12):
        start_point = (490, 350)
        angle = (i * 30) - 60
        length = 250
        end_x = start_point[0] + length * math.cos(math.radians(angle))
        end_y = start_point[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
# Tekst på uret
        numbers = ["1" , "2" ,"3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(numbers[i],True, black)
        textRect = text.get_rect()
        textRect.center = (end_x, end_y)
        screen.blit(text,textRect)


#Kanten på uret
    pygame.draw.circle(screen, black, (490, 350), 295, 5)


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()