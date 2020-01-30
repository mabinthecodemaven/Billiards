
import math
import pygame
pygame.init()

win = pygame.display.set_mode((1579, 873))
pygame.display.set_caption('Big Chungus')

bg = pygame.image.load('table.png')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('ebrima', 16)

board_u = 85
board_d = 751
board_l = 86
board_r = 1459

class Ball():
    def __init__(self, number):
        self.number = number
        self.x = 300
        self.y = 500

        self.x_vel = -8
        self.y_vel = 7




    def draw(self):
        if self.number <= 8:


            colors = {1: (255, 158, 3)}
            pygame.draw.ellipse(win, colors[self.number], (self.x, self.y, 36, 36))
            label = myfont.render(str(self.number), True, (0,0,0))
            win.blit(label, (self.x+14, self.y+5))

    def move(self):
        if math.hypot(self.x_vel, self.y_vel) > .6:

            ### Section handles x reflections
            if self.x + self.x_vel > board_r:
                self.x = board_r
                self.y += (abs(self.x - board_r) / self.x_vel) * self.y_vel
                self.x_vel *= -.9

            if self.x + self.x_vel < board_l:
                self.x = board_l
                self.y += (abs(self.x - board_l) / self.x_vel) * self.y_vel
                self.x_vel *= -.9

            ### Section handles y reflections
            if self.y + self.y_vel > board_d:
                self. y = board_d
                self.x += (abs(self.y - board_d) / self.y_vel) * self.x_vel
                self.y_vel *= -.9

            if self.y + self.y_vel < board_u:
                self.y = board_u
                self.x += (abs(self.y - board_u) / self.y_vel) * self.x_vel
                self.y_vel *= -.9

            self.x += self.x_vel
            self.y += self.y_vel
            self.y_vel *= .987
            self.x_vel *= .987

            if math.hypot(self.x_vel, self.y_vel) < 1.2:
                self.y_vel *= .987
                self.x_vel *= .987




one = Ball(1)

def redrawGameWindow():
    one.move()
    win.blit(bg,(0,0))

    one.draw()

    pygame.display.update()


running = True

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redrawGameWindow()

    clock.tick(25)



