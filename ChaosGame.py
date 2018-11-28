import pygame
import random

displayWidth = 0
displayHeight = 0

pygame.init()

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.toggle_fullscreen = True

info = pygame.display.Info()
while True:
    startPoints = []
    nextMove = 0
    corners = 3

    for i in range(corners):
        startPoints.append([random.randrange(0, info.current_w), random.randrange(0, info.current_h)])

    lastPoint = [random.randrange(0, info.current_w), random.randrange(0, info.current_h)]
    index = 0
    size = 2

    display.fill((0, 0, 0))

    for i in startPoints:
        pygame.draw.circle(display, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), i,
                           size, size)

    while index != 3500:
        index += 1

        nextMove = random.randrange(0, corners)

        lastPoint = [startPoints[nextMove][0] + (lastPoint[0] - startPoints[nextMove][0])/2, startPoints[nextMove][1] +
                     (lastPoint[1] - startPoints[nextMove][1])/2]

        pygame.draw.circle(display, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
                           (round(lastPoint[0]), round(lastPoint[1])), size, size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
