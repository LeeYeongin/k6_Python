import sys
import pygame
from util import init, handle_key_event, update_bullet, render
from setting import *

pygame.init()

screen, clock, image, screen_rect, ship_rect, bullets = init() # 우주선 위치 지정

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # raise SystemExit와 동일
        elif event.type == pygame.KEYDOWN:
            handle_key_event(ship_rect, bullets, event) 

    # Do logical updates here. 
    ### 1. 키보드 마우스 이벤트
    ### 2. 위치 update
    new_bullets = update_bullet(screen_rect, bullets)
            
    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    render(screen, image, ship_rect, new_bullets)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(FRAME_PER_SECOND)         # wait until next frame (at 60 FPS)
