from setting import HEIGHT, SHIP_IMAGE_PATH, WIDTH, SHIP_SPEED, BULLET_COLOR
import pygame


def init():
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    clock = pygame.time.Clock()
    image = pygame.image.load(SHIP_IMAGE_PATH) # 이미지 로드
    bullets = [] # 총알 수가 많으므로 list 사용

    # 직사각형 각도 좌표를 저장하는 파이게임 객체
    # rect = pygame.Rect((1280/2, 720/2), (200, 200)) # Rect((left, top), (width, height))
    screen_rect = screen.get_rect()
    ship_rect = image.get_rect()
    # 직접 따로 지정도 가능
    # ship_rect.left = 1280/2 
    # ship_rect.top = 600
    
    ship_rect.midbottom = screen.get_rect().midbottom
    return screen,clock,image,screen_rect,ship_rect, bullets

def create_bullet(ship_rect): # 총알 생성 함수
    bullet = pygame.Rect((0,0),(5,20)) # 총알을 직사각형을 그려 사용
    bullet.midbottom = ship_rect.midtop # 총알 위치 지정
    return bullet

def handle_key_event(ship_rect, bullets, event):
    if event.key == pygame.K_LEFT:
        ship_rect.left -= SHIP_SPEED
    elif event.key == pygame.K_RIGHT:
        ship_rect.right += SHIP_SPEED 
    # elif event.key == pygame.K_UP:
    #     ship_rect.top -= SHIP_SPEED
    # elif event.key == pygame.K_DOWN:
    #     # if ship_rect.bottom <= screen_rect.bottom:
    #     if (ship_rect.top + ship_rect.height) <= screen_rect.height: 
    #         ship_rect.bottom += SHIP_SPEED
    elif event.key == pygame.K_SPACE:
        bullets.append(create_bullet(ship_rect)) # 총알 생성 후 list에 추가

def update_bullet(screen_rect, bullets):
    new_bullets = []
    for bullet in bullets:
        if screen_rect.top < bullet.top: # 총알이 화면 안에 있을 경우만 -1, 아니면 사라짐
            bullet.top -= 10 # 총알이 앞으로 발사되도록
            new_bullets.append(bullet)
    return new_bullets

def render(screen, image, ship_rect, new_bullets):
    screen.blit(image, ship_rect)
    for bullet in new_bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)
