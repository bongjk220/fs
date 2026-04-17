import pygame, random, sys

WIDTH, HEIGHT = 600, 800
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stage Shooting Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

def create_explosion_frames():
    frames = []
    for radius in range(5, 25, 5):
        surf = pygame.Surface((50,50), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, random.randint(100,255), 0), (25,25), radius)
        frames.append(surf)
    return frames

explosion_frames = create_explosion_frames()

def create_enemy_image(type_id):
    if type_id == 1:
        img = pygame.image.load("py_game/enemy1.png").convert_alpha()
        img = pygame.transform.scale(img, (40,40))  # 크기 줄이기        
    elif type_id == 2:
        img = pygame.image.load("py_game/enemy2.png").convert_alpha()
        img = pygame.transform.scale(img, (40,40))  # 크기 줄이기
    elif type_id == 3:
        img = pygame.image.load("py_game/enemy3.png").convert_alpha()
        img = pygame.transform.scale(img, (40,40))  # 크기 줄이기
    return img
    # surf = pygame.Surface((40,40), pygame.SRCALPHA)
    # if type_id == 1:  # 벌레 모양
    #     # 몸통
    #     pygame.draw.ellipse(surf, (0,200,0), (10,10,20,15))  
    #     # 머리
    #     pygame.draw.circle(surf, (0,150,0), (20,8), 6)
    #     # 다리
    #     pygame.draw.line(surf, (0,100,0), (10,15), (0,5), 2)
    #     pygame.draw.line(surf, (0,100,0), (30,15), (40,5), 2)
    #     pygame.draw.line(surf, (0,100,0), (10,20), (0,30), 2)
    #     pygame.draw.line(surf, (0,100,0), (30,20), (40,30), 2)
    # elif type_id == 2:
    #     # 다른 벌레 변형
    #     pygame.draw.ellipse(surf, (150,50,0), (5,5,30,20))
    #     pygame.draw.circle(surf, (200,100,0), (20,25), 8)
    # elif type_id == 3:
    #     # 또 다른 벌레 변형
    #     pygame.draw.ellipse(surf, (50,0,150), (8,8,24,24))
    #     pygame.draw.line(surf, (80,0,180), (8,20), (0,10), 2)
    #     pygame.draw.line(surf, (80,0,180), (32,20), (40,10), 2)
    # return surf

def create_ship_image():
    img = pygame.image.load("py_game/my_ship.png").convert_alpha()
    img = pygame.transform.scale(img, (60,60))  # 크기 조정
    return img
    # surf = pygame.Surface((60,60), pygame.SRCALPHA)
    # pygame.draw.polygon(surf, (0,200,255), [(30,0),(0,60),(60,60)])
    # pygame.draw.rect(surf, (255,255,255), (25,20,10,30))
    # return surf

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.frames = explosion_frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=center)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]
                self.rect = self.image.get_rect(center=self.rect.center)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = create_ship_image()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.lives = 3
        self.weapon_level = 1
        self.last_shot = pygame.time.get_ticks()  # 마지막 발사 시각
        self.shoot_delay = 200  # 발사 간격(ms) → 200ms = 0.2초

    def update(self):
        mouse_x = pygame.mouse.get_pos()[0]
        self.rect.centerx += (mouse_x - self.rect.centerx) * 0.25
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH
    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:  # 쿨다운 체크
            self.last_shot = now
            offsets = []
            spread = 10
            if self.weapon_level == 1:
                offsets = [0]
            else:
                for i in range(self.weapon_level):
                    offset = - (self.weapon_level-1)*spread//2 + i*spread
                    offsets.append(offset)
            for offset in offsets:
                bullet = Bullet(self.rect.centerx+offset, self.rect.top, self.weapon_level)
                all_sprites.add(bullet)
                bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, stage):
        super().__init__()
        self.type_id = random.choice([1,2,3])
        self.image = create_enemy_image(self.type_id)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-40)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(3,7) + stage//10
        self.score_value = {1:10, 2:20, 3:50}[self.type_id]
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH-40)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(3,7)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, level=1):
        super().__init__()
        colors = [
            (255,255,0,100),   # 노란색 반투명
            (255,165,0,100),   # 주황색 반투명
            (255,0,0,100),     # 빨강 반투명
            (0,0,255,100),     # 파랑 반투명
            (128,0,128,100)    # 보라 반투명
        ]
        color = colors[min(level-1, len(colors)-1)]
        width = 6 + level
        height = 20 + level*2
        self.image = pygame.Surface((width,height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0,0,width,height))
        self.rect = self.image.get_rect(centerx=x, bottom=y)
        self.speedy = -8

    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class WeaponItem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill((255,215,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.speedy = 3
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

def spawn_enemies(stage):
    num_enemies = min(10 + stage, 50)
    for i in range(num_enemies):
        enemy = Enemy(stage)
        all_sprites.add(enemy)
        enemies.add(enemy)

def game_loop():
    global all_sprites, bullets, enemies
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    items = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    stage = 1
    target_score = 5000
    score = 0
    high_scores = []
    items_spawned = 0

    # 적군 초기화
    enemies.empty()
    all_sprites.remove(enemies)
    spawn_enemies(stage)

    running = True
    while running and stage <= 100:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_pressed()[0]:
            player.shoot()

        all_sprites.update()
        explosions.update()
        items.update()

        hits = pygame.sprite.groupcollide(enemies, bullets, True, False)
        for hit in hits:
            score += hit.score_value
            explosion = Explosion(hit.rect.center)
            all_sprites.add(explosion)
            explosions.add(explosion)
            # 아이템 드랍 확률 및 제한
            if random.random() < 0.05 and items_spawned < 2:
                item = WeaponItem(hit.rect.centerx, hit.rect.centery)
                all_sprites.add(item)
                items.add(item)
                items_spawned += 1
            enemy = Enemy(stage)
            all_sprites.add(enemy)
            enemies.add(enemy)

        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            player.lives -= 1
            explosion = Explosion(player.rect.center)
            all_sprites.add(explosion)
            explosions.add(explosion)
            if player.lives <= 0:
                high_scores.append(score)
                high_scores = sorted(high_scores, reverse=True)[:5]
                return score, high_scores
            else:
                # ✅ 플레이어만 위치 리셋 (총알 그룹은 그대로 유지)
                player.rect.centerx = WIDTH // 2
                player.rect.bottom = HEIGHT - 20
                # bullets 그룹이나 all_sprites.remove(bullets)는 절대 호출하지 않음

        hits = pygame.sprite.spritecollide(player, items, True)
        for hit in hits:
            player.weapon_level += 1

        if score >= target_score:
            screen.fill(BLACK)
            clear_text = font.render(f"Stage {stage} Clear!", True, WHITE)
            screen.blit(clear_text, (WIDTH//2 - 100, HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(2000)

            stage += 1
            target_score *= 2  # 스테이지 목표 점수 2배 증가
            items_spawned = 0  # 아이템 카운트 초기화

            screen.fill(BLACK)
            start_text = font.render(f"Stage {stage} Start!", True, WHITE)
            screen.blit(start_text, (WIDTH//2 - 100, HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(2000)

            # 스테이지 클리어 시 적군 초기화
            for e in enemies:
                all_sprites.remove(e)   # 전체 스프라이트 그룹에서도 제거
            enemies.empty()             # 적군 그룹 비우기
            spawn_enemies(stage)        # 새 적군 생성

        # 화면 그리기
        screen.fill(BLACK)
        all_sprites.draw(screen)
        explosions.draw(screen)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
        stage_text = font.render(f"Stage: {stage}", True, WHITE)
        weapon_text = font.render(f"Weapon Lv: {player.weapon_level}", True, WHITE)
        screen.blit(score_text, (10,10))
        screen.blit(lives_text, (WIDTH-120,10))
        screen.blit(stage_text, (WIDTH//2 - 50,10))
        screen.blit(weapon_text, (10,40))
        pygame.display.flip()

def main():
    while True:
        score, high_scores = game_loop()

        # 게임 오버 화면 루프
        waiting = True
        while waiting:
            screen.fill(BLACK)
            over_text = font.render("Game Over!", True, WHITE)
            score_text = font.render(f"Your Score: {score}", True, WHITE)
            high_text = font.render("Top 5 Scores:", True, WHITE)

            screen.blit(over_text, (WIDTH//2 - 80, HEIGHT//2 - 120))
            screen.blit(score_text, (WIDTH//2 - 100, HEIGHT//2 - 80))
            screen.blit(high_text, (WIDTH//2 - 100, HEIGHT//2 - 40))

            # Top 5 점수 표시
            for i, s in enumerate(high_scores):
                hs_text = font.render(f"{i+1}. {s}", True, WHITE)
                screen.blit(hs_text, (WIDTH//2 - 80, HEIGHT//2 + i*30))

            restart_text = font.render("Press R to Restart", True, WHITE)
            quit_text = font.render("Press Q to Quit", True, WHITE)
            screen.blit(restart_text, (WIDTH//2 - 100, HEIGHT//2 + 200))
            screen.blit(quit_text, (WIDTH//2 - 100, HEIGHT//2 + 240))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False   # 다시 시작
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()
