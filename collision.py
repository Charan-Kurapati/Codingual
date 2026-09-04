import math
import random
import pygame

pygame.init()
pygame.mixer.init()

explosion = pygame.mixer.Sound("explosion.wav")

# -------------------------
# Screen
# -------------------------

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Space Invader")

clock = pygame.time.Clock()

# -------------------------
# Load images
# -------------------------

background = pygame.image.load("space.png")
playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")

# Resize sprites
playerImg = pygame.transform.scale(
    playerImg, (64, 64)
)

enemyImg = pygame.transform.scale(
    enemyImg, (64, 64)
)

# -------------------------
# Player
# -------------------------

playerX = random.randint(
    0,
    SCREEN_WIDTH - 64
)

playerY = random.randint(
    0,
    SCREEN_HEIGHT - 64
)

# -------------------------
# Enemies
# -------------------------

num_of_enemies = 7

enemyX = []
enemyY = []
enemyDX = []
enemyDY = []

enemyVisible = []

# 23 degree angle
angle = math.radians(23)

speed = 5

for i in range(num_of_enemies):

    enemyX.append(
        random.randint(0, SCREEN_WIDTH - 64)
    )

    enemyY.append(
        random.randint(0, SCREEN_HEIGHT - 64)
    )

    directionX = random.choice([-1, 1])
    directionY = random.choice([-1, 1])

    enemyDX.append(
        speed * math.cos(angle) * directionX
    )

    enemyDY.append(
        speed * math.sin(angle) * directionY
    )

    enemyVisible.append(True)

# -------------------------
# Player movement
# -------------------------

playerDX = speed * math.cos(angle)
playerDY = speed * math.sin(angle)

if random.choice([True, False]):
    playerDX *= -1

if random.choice([True, False]):
    playerDY *= -1

# -------------------------
# Score
# -------------------------

score = 0

font = pygame.font.Font(
    "freesansbold.ttf",
    32
)

# -------------------------
# Game loop
# -------------------------

running = True

while running:

    # -------------------------
    # Background
    # -------------------------

    screen.fill((0, 0, 0))

    screen.blit(
        background,
        (0, 0)
    )

    # -------------------------
    # Events
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # -------------------------
    # Move player
    # -------------------------

    playerX += playerDX
    playerY += playerDY

    # Player bounces left/right
    if playerX <= 0:
        playerX = 0
        playerDX *= -1

    if playerX >= SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64
        playerDX *= -1

    # Player bounces top/bottom
    if playerY <= 0:
        playerY = 0
        playerDY *= -1

    if playerY >= SCREEN_HEIGHT - 64:
        playerY = SCREEN_HEIGHT - 64
        playerDY *= -1

    # -------------------------
    # Player rectangle
    # -------------------------

    playerRect = playerImg.get_rect(
        topleft=(playerX, playerY)
    )

    # -------------------------
    # Move enemies
    # -------------------------

    for i in range(num_of_enemies):

        if enemyVisible[i]:

            enemyX[i] += enemyDX[i]
            enemyY[i] += enemyDY[i]

            # Enemy bounces left/right
            if enemyX[i] <= 0:
                enemyX[i] = 0
                enemyDX[i] *= -1

            if enemyX[i] >= SCREEN_WIDTH - 64:
                enemyX[i] = SCREEN_WIDTH - 64
                enemyDX[i] *= -1

            # Enemy bounces top/bottom
            if enemyY[i] <= 0:
                enemyY[i] = 0
                enemyDY[i] *= -1

            if enemyY[i] >= SCREEN_HEIGHT - 64:
                enemyY[i] = SCREEN_HEIGHT - 64
                enemyDY[i] *= -1

            # -------------------------
            # Collision
            # -------------------------

            enemyRect = enemyImg.get_rect(
                topleft=(enemyX[i], enemyY[i])
            )

            if playerRect.colliderect(enemyRect):

                # Increase score
                score += 1

                # Play explosion sound
                explosion.play()

                # Move enemy to random position
                enemyX[i] = random.randint(
                    0,
                    SCREEN_WIDTH - 64
                )

                enemyY[i] = random.randint(
                    0,
                    SCREEN_HEIGHT - 64
                )

                # Give enemy a new direction
                directionX = random.choice([-1, 1])
                directionY = random.choice([-1, 1])

                enemyDX[i] = (
                    speed * math.cos(angle) * directionX
                )

                enemyDY[i] = (
                    speed * math.sin(angle) * directionY
                )

    # -------------------------
    # Draw player
    # -------------------------

    screen.blit(
        playerImg,
        (playerX, playerY)
    )

    # -------------------------
    # Draw enemies
    # -------------------------

    for i in range(num_of_enemies):

        if enemyVisible[i]:

            screen.blit(
                enemyImg,
                (enemyX[i], enemyY[i])
            )

    # -------------------------
    # Display score
    # -------------------------

    scoreText = font.render(
        "Score: " + str(score),
        True,
        (255, 255, 255)
    )

    screen.blit(
        scoreText,
        (10, 10)
    )

    # -------------------------
    # Update screen
    # -------------------------

    pygame.display.update()

    clock.tick(60)

pygame.quit()
