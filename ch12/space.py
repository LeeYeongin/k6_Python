import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./images/ship.bmp')
rect = image.get_rect()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # raise SystemExit
            sys.exit()

    # Do logical updates here. 
    ### 1. 키보드 마우스 이벤트
    ### 2. 위치 update
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    screen.blit(image, rect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
