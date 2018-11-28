import pygame
import random
import time

displayWidth = 1300
displayHeight = 700

pygame.init()

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.toggle_fullscreen = True

info = pygame.display.Info()
startPoints = []
nextMove = 0
points = []
b1 = b2 = 0
m1 = m2 = 0

corners = 3
 
for i in range(corners):
    a1 = random.randrange(0, info.current_w)
    a2 = random.randrange(0, info.current_h)
    startPoints.append([a1, a2])
    if a1 > b1:
        b1 = a1
    if a2 > b2:
        b2 = a2
    if a1 < m1:
        m1 = a1
    if a2 < m2:
        m2 = a2

h = b2 - m2
h2 = random.randrange(m2, b2)
rap = (h2 - m2)/h
w = b1 - m1
w2 = m1 + w * rap/2
w3 = b1 - w * rap/2
points.append([random.randrange(round(w2), round(w3)), h2])

while True:
    pygame.display.toggle_fullscreen = True
    for i in startPoints:
        pygame.draw.circle(display, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), i, 1, 1)

    nextMove = random.randrange(0, corners)

    lastPoint = points[len(points) - 1]
    points.append([startPoints[nextMove][0] + (lastPoint[0] - startPoints[nextMove][0])/2, startPoints[nextMove][1] + (lastPoint[1] - startPoints[nextMove][1])/2])
    
    for i in points:
        pygame.draw.circle(display, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), (round(i[0]), round(i[1])), 1, 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()
