import pygame, time
x=0

wind=pygame.display.set_mode([500,500])
wind.fill([78, 123, 45])
pygame.draw.rect(wind, [55, 255, 20], [10, 20, 30, 40])
pygame.draw.circle(wind, [91, 80, 255], [250, 250], 10)


while True:
    time.sleep(1/60)
    wind.fill([78, 123, 45])
    x+=1
    pygame.draw.circle(wind, [91, 80, 255], [250, x], 10)

    pygame.display.flip()
    pygame.event.get()
