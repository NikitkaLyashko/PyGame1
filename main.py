import pygame

enot=pygame.image.load("enot.png")
enot=pygame.transform.scale(enot,[100,100])
wind=pygame.display.set_mode([500,500])

while True:
    wind.fill([78, 123, 45])
    wind.blit(enot, [0, 0])
    pygame.draw.rect(wind, [55, 255, 20], [10, 20, 30, 40])
    pygame.draw.circle(wind, [91, 80, 255], [250, 250], 10)
    pygame.image.save(wind, "a.png")
    pygame.display.flip()
    pygame.event.get()
