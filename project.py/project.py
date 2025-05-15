import pygame
import random
import sys

pygame.init()

# Stałe
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (200, 50, 50)
BLACK = (0, 0, 0)
BLUE = (100, 100, 250)

# Ustawienia gry
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
player_speed = 10
obstacle_speed = 5
spawn_rate = 30
font = pygame.font.SysFont(None, 35)

# Inicjalizacja okna
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner Game")


def display_message(text, color, y_offset=0):
    message = font.render(text, True, color)
    rect = message.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_offset))
    win.blit(message, rect)


def reset_game():
    player = pygame.Rect(100, HEIGHT - 100, PLAYER_SIZE, PLAYER_SIZE)
    obstacles = []
    score = 0
    level = 1
    obstacle_speed = 5
    spawn_rate = 30
    game_active = True
    return player, obstacles, score, level, obstacle_speed, spawn_rate, game_active


def move_player(player, keys, level):
    global player_speed
    if level >= 7:  # Jeśli poziom to 7 lub wyższy, zwiększ prędkość
        player_speed = 17
    if keys[pygame.K_LEFT] and player.x - player_speed > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x + player_speed < WIDTH - PLAYER_SIZE:
        player.x += player_speed


def spawn_obstacle(obstacles):
    if random.randint(1, spawn_rate) == 1:
        obstacles.append(pygame.Rect(random.randint(0, WIDTH - OBSTACLE_SIZE), 0, OBSTACLE_SIZE, OBSTACLE_SIZE))
    return obstacles


def update_score(score, level, obstacle_speed, spawn_rate):
    score += 1
    if score % 15 == 0:
        level += 1
        obstacle_speed += 2
        spawn_rate = max(15, spawn_rate - 5)
    return score, level, obstacle_speed, spawn_rate


def check_collision(player, obstacles):
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            return True
    return False


def main():
    global player_speed
    clock = pygame.time.Clock()
    player, obstacles, score, level, obstacle_speed, spawn_rate, game_active = reset_game()

    running = True
    while running:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player, obstacles, score, level, obstacle_speed, spawn_rate, game_active = reset_game()

        if not game_active:
            display_message(f"Game Over! Your score: {score}", BLACK, -30)
            display_message("Press SPACE to Start", BLACK, 30)
            pygame.display.flip()
            continue

        keys = pygame.key.get_pressed()
        move_player(player, keys, level)  # Przekazujemy player, keys i level
        obstacles = spawn_obstacle(obstacles)

        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
                score, level, obstacle_speed, spawn_rate = update_score(score, level, obstacle_speed, spawn_rate)  # Aktualizujemy zmienne

        if check_collision(player, obstacles):  # Przekazujemy player i obstacles
            game_active = False

        pygame.draw.rect(win, BLUE, player)
        for obstacle in obstacles:
            pygame.draw.rect(win, RED, obstacle)

        score_text = font.render("Score: " + str(score), True, BLACK)
        level_text = font.render("Level: " + str(level), True, BLACK)
        win.blit(score_text, (10, 10))
        win.blit(level_text, (10, 40))

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
