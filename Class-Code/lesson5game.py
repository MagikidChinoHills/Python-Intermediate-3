import pygame, sys, random

pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Player setup
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Block setup
block_size = 50
blocks = []
initial_block_speed = 5
block_speed = initial_block_speed

score = 0
game_over = False

def spawn_block():
    x = random.randint(0, WIDTH - block_size)
    y = -block_size
    return pygame.Rect(x, y, block_size, block_size)

# Start with 1 block
blocks.append(spawn_block())

def draw(player, blocks):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for block in blocks:
        pygame.draw.rect(screen, (255, 0, 0), block)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

while True:
    if game_over:
        screen.fill((0, 0, 0))
        text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 160, HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                player_x = WIDTH // 2 - player_size // 2
                blocks = [spawn_block()]
                score = 0
                block_speed = initial_block_speed
                game_over = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    for block in blocks:
        block.y += int(block_speed)

        if block.y > HEIGHT:
            block.y = -block_size
            block.x = random.randint(0, WIDTH - block_size)
            score += 1
            block_speed += 0.05  # gradual difficulty increase

            # Every 10 points, add a new block
            if score % 10 == 0:
                blocks.append(spawn_block())

    for block in blocks:
        if player_rect.colliderect(block):
            game_over = True

    draw(player_rect, blocks)
    clock.tick(60)
