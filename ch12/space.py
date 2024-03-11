import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./images/ship.bmp') # 이미지 로드
# 직사각형 각도 좌표를 저장하는 파이게임 객체
# rect = pygame.Rect((1280/2, 720/2), (200, 200)) # Rect((left, top), (width, height))
image_rect = image.get_rect()
# 직접 지정해줄 수 있음
# image_rect.left = 1280/2 
# image_rect.top = 600
image_rect.midbottom = screen.get_rect().midbottom

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
    # screen.blit(image, image_rect)
    screen.blit(image, image_rect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
