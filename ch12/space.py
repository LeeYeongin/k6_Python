import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./images/ship.bmp') # 이미지 로드
# 직사각형 각도 좌표를 저장하는 파이게임 객체
# rect = pygame.Rect((1280/2, 720/2), (200, 200)) # Rect((left, top), (width, height))
screen_rect = screen.get_rect()
ship_rect = image.get_rect()
# 직접 지정해줄 수 있음
# image_rect.left = 1280/2 
# image_rect.top = 600

ship_rect.midbottom = screen.get_rect().midbottom
def create_bullet(ship_rect): # 총알 생성 함수
    bullet = pygame.Rect((0,0),(5,20)) # 총알을 직사각형을 그려 사용
    bullet.midbottom = ship_rect.midtop # 총알 위치 지정
    return bullet

bullets = [] # 총알 수가 많으므로 list 사용
# bullet = create_bullet(ship_rect) 
bullet_color = (255, 0, 0) # 총알 색 지정


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # raise SystemExit와 동일
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_rect.left -= 5
            elif event.key == pygame.K_RIGHT:
                ship_rect.right += 5
            # elif event.key == pygame.K_UP:
            #     ship_rect.top -= 5
            # elif event.key == pygame.K_DOWN:
            #     # if ship_rect.bottom <= screen_rect.bottom:
            #     if (ship_rect.top + ship_rect.height) <= screen_rect.height: 
            #         ship_rect.bottom += 5
            elif event.key == pygame.K_SPACE:
                bullets.append(create_bullet(ship_rect)) # 총알 생성 후 list에 추가
            

    # Do logical updates here. 
    ### 1. 키보드 마우스 이벤트
    ### 2. 위치 update
    new_bullets = []
    for bullet in bullets:
        if screen_rect.top < bullet.top:
            bullet.top -= 1 # 총알이 앞으로 발사되도록
            new_bullets.append(bullet)
            
    screen.fill("purple")  # Fill the display with a solid color


    # Render the graphics here.
    # screen.blit(image, rect)
    screen.blit(image, ship_rect)
    for bullet in new_bullets:
        pygame.draw.rect(screen, bullet_color, bullet)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
