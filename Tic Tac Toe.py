# Tic Tac Toe

import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((300,400))
pygame.display.set_caption('Tic Tac Toe')


class SquareBox:
    
    def __init__(self, screen, x_coordinate, y_coordinate, x_size, y_size, state = True, player_no = 0):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.x_size = x_size
        self.y_size = y_size
        self.screen = screen
        self.state = state
        self.player_no = player_no
        
    def click(self):
        if self.player_no == 0:
            pygame.draw.circle(self.screen, (255,0,0), (int(self.x_coordinate + (self.x_size/2)), int(self.y_coordinate + (self.y_size/2))), 30, 10)
        elif self.player_no == 1:
            pygame.draw.line(self.screen, (0,255,0), (int(self.x_coordinate + 20), int(self.y_coordinate + 20)), (int(self.x_coordinate + self.x_size - 20), int(self.y_coordinate + self.y_size - 20)), 10)
            pygame.draw.line(self.screen, (0,255,0), (int(self.x_coordinate + 20), int(self.y_coordinate + self.y_size - 20)),(int(self.x_coordinate + self.x_size - 20), int(self.y_coordinate + 20)), 10)
           
  
def draw_background(screen):
    pygame.draw.line(screen,(0,0,255), (100,50),(100,350), 5)
    pygame.draw.line(screen,(0,0,255), (200,50),(200,350), 5)
    pygame.draw.line(screen,(0,0,255), (25,150),(275,150), 5)
    pygame.draw.line(screen,(0,0,255), (25,250),(275,250), 5)
               
def click_box(position_list, box, mouse_position):
    box_coordinates = [(5, 50),(106, 50),(206, 50),(5, 156),(106, 156),(206, 156),(5, 255),(106, 255),(206, 255)]
    
    if box.state == True:
        if (box.x_coordinate) <= mouse_position[0] <= (box.x_coordinate + box.x_size):
            if (box.y_coordinate) <= mouse_position[1] <= (box.y_coordinate + box.y_size):
                click = (box.x_coordinate,box.y_coordinate)
                box.state = False
                click = box_coordinates.index(click)
                position_list.append(click)
                if len(position_list)%2 == 0:
                    player_no = 0
                else:
                    player_no = 1
                box.player_no = player_no
                box.click()
                return player_no, click, position_list
                
def check_result(click, player_no, check_list):
    check_list[click] = player_no
    a = check_list.reshape(3,3)
   
    if a[0,0]==a[1,1]==a[2,2]:
        pygame.draw.line(screen,(0,255,255), (50,97.5),(251,302.5), 5)
        return False
    elif a[0,2]==a[1,1]==a[2,0]:
        pygame.draw.line(screen,(0,255,255), (251,97.5),(50,302.5), 5)
        return False
    else:
        for i in range(3):
            if a[i,0]==a[i,1]==a[i,2]:
                if i == 0:
                    pygame.draw.line(screen,(0,255,255), (50,97.5),(251,97.5), 5)
                    return False
                elif i == 1:
                    pygame.draw.line(screen,(0,255,255), (50,203.5),(251,203.5), 5)
                    return False
                elif i == 2:
                    pygame.draw.line(screen,(0,255,255), (50,302.5),(251,302.5), 5)
                    return False
            elif a[0,i]==a[1,i]==a[2,i]:
                if i == 0:
                    pygame.draw.line(screen,(0,255,255), (50,97.5),(50,302.5), 5)
                    return False
                elif i == 1:
                    pygame.draw.line(screen,(0,255,255), (151,95.5),(151,302.5), 5)
                    return False
                elif i == 2:
                    pygame.draw.line(screen,(0,255,255), (251,97.5),(251,302.5), 5)
                    return False
 
def new_game(boxes_list):
    del(boxes_list)
    screen.fill((0,0,0))
    draw_background(screen)
    pygame.display.update()
 
def main():
    position_list = []
    check_list = np.arange(3,30,3)
    boxes_list = [SquareBox(screen, 5, 50, 90, 95),SquareBox(screen, 106, 50, 90, 95),SquareBox(screen, 206, 50, 90, 95),SquareBox(screen, 5, 156, 90, 90),SquareBox(screen, 106, 156, 90, 90),SquareBox(screen, 206, 156, 90, 90),SquareBox(screen, 5, 255, 90, 95),SquareBox(screen, 106, 255, 90, 95),SquareBox(screen, 206, 255, 90, 95)]
    draw_background(screen)
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_focused() == 1:
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if pygame.mouse.get_pressed() == (1, 0, 0):
                         mouse_position = pygame.mouse.get_pos()
                         for i,box in enumerate(boxes_list):
                             click = click_box(position_list, box, mouse_position)
                             if type(click) == tuple:
                                 player_no = click[0]
                                 click_1 = click[1]
                                 position_list = click[2]
                         try:
                             check = check_result(click_1, player_no, check_list)
                         except UnboundLocalError:
                             pass
        pygame.display.update()
        try:
            if check == False or len(position_list) == 9:
                    pygame.time.delay(2000)
                    check = new_game(boxes_list)
                    position_list = []
                    check_list = np.arange(3,30,3)
                    boxes_list = [SquareBox(screen, 5, 50, 90, 95),SquareBox(screen, 106, 50, 90, 95),SquareBox(screen, 206, 50, 90, 95),SquareBox(screen, 5, 156, 90, 90),SquareBox(screen, 106, 156, 90, 90),SquareBox(screen, 206, 156, 90, 90),SquareBox(screen, 5, 255, 90, 95),SquareBox(screen, 106, 255, 90, 95),SquareBox(screen, 206, 255, 90, 95)]
        except UnboundLocalError:
            pass
            
if __name__:'__main__', main()

            
        
