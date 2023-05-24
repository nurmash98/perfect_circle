import pygame
import numpy as np
pygame.init()
import math

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Draw a Perfect Circle")
font = pygame.font.Font(None, 36)
percentage = 0
color = (255, 0, 0)
drawing = False
points = []
radiuses = []
center_x, center_y = window_width // 2, window_height // 2
perfect_radius = None
running = True
sum_diffs = 0

text_content = "XX%"
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                time = int(pygame.time.get_ticks())//1000
                point_x, point_y = pygame.mouse.get_pos()
                drawing = True
                points.clear()
                radiuses = []
                percentage = 0
                points.append(pygame.mouse.get_pos())
                perfect_radius = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            # if time == 0:
            #     time = pygame.time.get_ticks()
            # elif pygame.time.get_ticks() - time >= 10:
            #     text_content = "Your time is up! Restart"
            #     drawing = False
            #     time = 0
            if drawing:
                if int(pygame.time.get_ticks())//1000 - 10 > time:
                    text_content = "Your time is up! Restart"
                    drawing = False
                point_x, point_y = pygame.mouse.get_pos()
                point = (point_x, point_y)
                if point in points:
                    drawing = False
                n = len(points)
                th_percent = 15
                radius = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)
                radiuses.append(radius)
                within_threshold = sum(abs(num - perfect_radius) <= perfect_radius * th_percent/ 100 for num in radiuses)                    
                percentage  = (within_threshold / len(radiuses))*100
                points.append(pygame.mouse.get_pos())
                text_content = f"{round(percentage, 3)}%"
                
                
            
#    within_threshold = sum(abs(num - perfect_number) <= perfect_number * threshold_percentage / 100
#                       for num in other_numbers)
# percentage_within_threshold = (within_threshold / len(other_numbers)) * 100
    window.fill((255, 255, 255))
    pygame.draw.circle(window, color, (center_x, center_y), 2)
    
    timer = font.render(f"{time} seconds", True, (0, 0, 0))
    text_surface = font.render(text_content, True, (0, 0, 0))
    window.blit(timer, (100, 100)) 
    window.blit(text_surface, (center_x, center_y)) 
   
    if len(points) > 1:
        pygame.draw.lines(window, (0, 0, 0), False, points, 2)

    pygame.display.flip()

# Quit the game
pygame.quit()
