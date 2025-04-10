import pygame

import random

# Thiết lập kích thước của sổ
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 144  # Cài số khung hình trên giây

BOW_MAN_IMAGE = pygame.image.load("bow.png")
BOW_MAN = pygame.transform.scale(BOW_MAN_IMAGE, (50, 50))
BOW_MAN_FLIPPED = pygame.transform.flip(BOW_MAN, True, False) 

AXE_MAN_IMAGE = pygame.image.load("axe.png")
AXE_MAN = pygame.transform.scale(AXE_MAN_IMAGE, (50, 50))
AXE_MAN_FLIPPED = pygame.transform.flip(AXE_MAN, True, False)

SWORD_MAN_IMAGE = pygame.image.load("sword.png")
SWORD_MAN = pygame.transform.scale(SWORD_MAN_IMAGE, (50, 50))
SWORD_MAN_FLIPPED = pygame.transform.flip(SWORD_MAN, True, False)

MAGIC_MAN_IMAGE = pygame.image.load("magic.png")
MAGIC_MAN = pygame.transform.scale(MAGIC_MAN_IMAGE, (50, 50))
MAGIC_MAN_FLIPPED = pygame.transform.flip(MAGIC_MAN, True, False)

VELOCITY = 5  # Kiểm soát tốc độ người chơi
BULLET_VELOCITY = 15  # tốc độ đạn
MAX_BULLETS = 5  # số lượng đạn mà nhân vật có thể bắn trong một lượt

# Tạo đối tượng hình chữ nhật pygame để điều khiển các nhân vật 
player_bow_user = pygame.Rect(200, 250, 50, 50)  # khởi tạo một pygame Rect (X, Y, chiều rộng, chiều cao)
# Tạo các đổi tượng hình chữ nhật pygame là npc
npc_magic_user = pygame.Rect(700, 50, 50, 50)
npc_axe_user = pygame.Rect(700, 200, 50, 50)
npc_sword_user = pygame.Rect(700, 400, 50, 50)


# Tạo một danh sách chứa hướng và khoảng cách của mỗi NPC
npc_info = [
    {"direction": random.choice(["left", "right", "up", "down"]), "distance": 30},  # NPC Magic
    {"direction": random.choice(["left", "right", "up", "down"]), "distance": 30},  # NPC Axe
    {"direction": random.choice(["left", "right", "up", "down"]), "distance": 30},  # NPC Sword
]


def npc_move_random(npc, npc_info, npc_index):
    # Lấy hướng và khoảng cách di chuyển cho NPC từ danh sách
    direction = npc_info[npc_index]["direction"]
    movement_distance = npc_info[npc_index]["distance"]

    if movement_distance > 0:
        if direction == "left" and npc.x > 0:  # Kiểm tra không đi ra ngoài trái
            npc.x -= VELOCITY
        elif direction == "right" and npc.x < WIDTH - npc.width:  # Kiểm tra không đi ra ngoài phải
            npc.x += VELOCITY
        elif direction == "up" and npc.y > 0:  # Kiểm tra không đi ra ngoài trên
            npc.y -= VELOCITY
        elif direction == "down" and npc.y < HEIGHT - npc.height:  # Kiểm tra không đi ra ngoài dưới
            npc.y += VELOCITY

        npc_info[npc_index]["distance"] -= VELOCITY  # Giảm khoảng cách sau mỗi bước di chuyển

    if npc_info[npc_index]["distance"] <= 0:
        npc_info[npc_index]["distance"] = 100  # Đặt lại khoảng cách di chuyển
        npc_info[npc_index]["direction"] = random.choice(["left", "right", "up", "down"])  # Chọn lại hướng di chuyển

    return npc_info


# Hàm xử lý di chuyển người chơi
def bow_man_movement_handle(key_pressed, player_bow_user):
    if key_pressed[pygame.K_a] and player_bow_user.x - VELOCITY > 0:  # kiểm tra phím nhập vào
        player_bow_user.x -= VELOCITY  # di chuyển trái
    elif key_pressed[pygame.K_d] and player_bow_user.x + VELOCITY + player_bow_user.width < WIDTH:
        player_bow_user.x += VELOCITY  # di chuyển phải
    elif key_pressed[pygame.K_w] and player_bow_user.y - VELOCITY > 0:
        player_bow_user.y -= VELOCITY  # di chuyển lên
    if key_pressed[pygame.K_s] and player_bow_user.y + VELOCITY + player_bow_user.height < HEIGHT:
        player_bow_user.y += VELOCITY  # di chuyển xuống

# Hàm vẽ cửa sổ và các đối tượng
def draw_window(player_bow_user, npc_magic_user, npc_axe_user, npc_sword_user, player_bow_user_bullets):
    WINDOW.fill(WHITE)
    WINDOW.blit(BOW_MAN, (player_bow_user.x, player_bow_user.y))
    WINDOW.blit(MAGIC_MAN_FLIPPED, (npc_magic_user.x, npc_magic_user.y))
    WINDOW.blit(AXE_MAN_FLIPPED, (npc_axe_user.x, npc_axe_user.y))
    WINDOW.blit(SWORD_MAN_FLIPPED, (npc_sword_user.x, npc_sword_user.y))

    for bullet in player_bow_user_bullets:
        pygame.draw.rect(WINDOW, BLACK, bullet)

    pygame.display.update()

# Hàm xử lý di chuyển viên đạn
def handle_bullets(bow_user_bullets):
    for bullet in bow_user_bullets:
        bullet.x += BULLET_VELOCITY  # Đạn di chuyển sang phải
        if bullet.y > HEIGHT:
            bow_user_bullets.remove(bullet)

# Sử dụng trong vòng lặp chính:
def main():
    global npc_info

    clock = pygame.time.Clock()
    run = True
    bow_user_bullets = []

    while run:
        clock.tick(FPS)  # Điều khiển số khung hình trên giây
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(bow_user_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_bow_user.x + player_bow_user.width / 2, player_bow_user.y + player_bow_user.height, 10, 5)
                    bow_user_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()

        # Di chuyển nhân vật người chơi
        bow_man_movement_handle(keys_pressed, player_bow_user)

        # Di chuyển NPC (dùng danh sách npc_info)
        npc_info = npc_move_random(npc_magic_user, npc_info, 0)  # NPC Magic
        npc_info = npc_move_random(npc_axe_user, npc_info, 1)    # NPC Axe
        npc_info = npc_move_random(npc_sword_user, npc_info, 2)   # NPC Sword

        handle_bullets(bow_user_bullets)
        draw_window(player_bow_user, npc_magic_user, npc_axe_user, npc_sword_user, bow_user_bullets)

    pygame.quit()

if __name__ == "__main__":
    main()

