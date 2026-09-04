import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

# Load images
background = pygame.image.load("space.png")
playerImg = pygame.image.load("player.png")
bulletImg = pygame.image.load("bullet.png")

# Game clock
clock = pygame.time.Clock()

# Player
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(
        random.randint(
            ENEMY_START_Y_MIN,
            ENEMY_START_Y_MAX
        )
    )
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render(
        "Score : " + str(score_value),
        True,
        (255, 255, 255)
    )
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state

    bullet_state = "fire"

    screen.blit(
        bulletImg,
        (x + 16, y + 10)
    )


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (enemyX - bulletX) ** 2 +
        (enemyY - bulletY) ** 2
    )

    return distance < COLLISION_DISTANCE


# Game loop
running = True
game_over = False

while running:

    # Background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # -------------------------
    # Events
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Keyboard pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            # Shoot
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        # Keyboard released
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                playerX_change = 0

            if event.key == pygame.K_RIGHT:
                playerX_change = 0

    # -------------------------
    # Game
    # -------------------------

    if not game_over:

        # Move player
        playerX += playerX_change

        # Keep player on screen
        if playerX <= 0:
            playerX = 0

        if playerX >= SCREEN_WIDTH - 64:
            playerX = SCREEN_WIDTH - 64

        # -------------------------
        # Enemies
        # -------------------------

        for i in range(num_of_enemies):

            # Game over
            if enemyY[i] > 340:

                for j in range(num_of_enemies):
                    enemyY[j] = 2000

                game_over = True
                break

            # Move enemy
            enemyX[i] += enemyX_change[i]

            # Enemy reaches edge
            if enemyX[i] <= 0:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            elif enemyX[i] >= SCREEN_WIDTH - 64:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            # -------------------------
            # Collision
            # -------------------------

            if bullet_state == "fire":

                if isCollision(
                    enemyX[i],
                    enemyY[i],
                    bulletX,
                    bulletY
                ):

                    bulletY = playerY
                    bullet_state = "ready"

                    score_value += 1

                    # Respawn enemy
                    enemyX[i] = random.randint(
                        0,
                        SCREEN_WIDTH - 64
                    )

                    enemyY[i] = random.randint(
                        ENEMY_START_Y_MIN,
                        ENEMY_START_Y_MAX
                    )

            # Draw enemy
            enemy(
                enemyX[i],
                enemyY[i],
                i
            )

        # -------------------------
        # Bullet
        # -------------------------

        if bullet_state == "fire":

            fire_bullet(
                bulletX,
                bulletY
            )

            bulletY -= bulletY_change

            # Bullet leaves screen
            if bulletY <= 0:
                bulletY = playerY
                bullet_state = "ready"

        # Draw player
        player(
            playerX,
            playerY
        )

        # Draw score
        show_score(
            textX,
            textY
        )

    else:

        # Game over
        game_over_text()

        # Show score
        show_score(
            textX,
            textY
        )

    # Update display
    pygame.display.update()

    # Keep game running at 60 FPS
    clock.tick(60)


pygame.quit()