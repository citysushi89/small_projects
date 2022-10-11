# space_invaders.py runs a space invaders clone


from unicodedata import name
import pygame
import random
import pyautogui
from pygame import mixer



# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((1000, 600))

# Title and Icon
pygame.display.set_caption("Federal Reserve Invaders")

# Background img
background = pygame.image.load("icons/fedres.jpg")
# Background sound
mixer.music.load("sounds/Goldeneye.mp3")
mixer.music.play(-1)


bank = pygame.image.load("icons/bank.png")
pygame.display.set_icon(bank)

# Player set up
player_icon = pygame.image.load("icons/gun.png")
player_x_pos = 470
player_y_pos = 480
player_x_change = 0

# Enemy set up
enemy_icon = []
enemy_x_pos = []
enemy_y_pos = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 8

for i in range(number_of_enemies):
    enemy_icon.append(pygame.image.load("icons/profits.png"))
    enemy_x_pos.append(random.randint(0, 936))
    enemy_y_pos.append(random.randint(50, 200))
    enemy_x_change.append(0.4)
    enemy_y_change.append(20)

print(enemy_icon)
# Bullet set up
bullet_icon = pygame.image.load("icons/bullets.png")
bullet_x_pos = 0
bullet_y_pos = 480
bullet_x_change = 0
bullet_y_change = 1
bullet_state = "ready"

# Score 
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x_pos = 10
text_y_pos = 10

# Game over text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    game_over_text = font.render("INEVITABLE. The bankers have one. GAME OVER: " + str(score_value), True, (255, 255, 255))
    screen.blit(game_over_text, (75, 75))

def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_icon[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bullet_icon, (x, y - 15))


pyautogui.alert("Quick! The ~Unnamed big bank~ is printing more money,\n"
                "devaluing the savings your family has worked decades to accumulate.\n"
                "Use your crew-served weapons to prevent the money from entering the supply"
                " and destroying what's left of your family's hard work!")

# Game Loop
running = True
while running:
    
    screen.fill((0, 0, 0))
    # Set up Background
    screen.blit(background, (-100, -100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Check for key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("sounds/gunfire.mp3")
                    bullet_sound.play()
                    bullet_sound.set_volume(.4)

                    bullet_x_pos = player_x_pos
                    fire_bullet(bullet_x_pos, bullet_y_pos)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Prevent player from running off screen
    player_x_pos += player_x_change

    if player_x_pos <= 0:
        player_x_pos = 0
    elif player_x_pos >= 936:
        player_x_pos = 936

    # Enemy movement
    for i in range(number_of_enemies):

        # Check for game over
        if enemy_y_pos[i] > 410:
            for j in range(number_of_enemies):
                enemy_y_pos[j] = 2000
            game_over_text()
            break

        enemy_x_pos[i] += enemy_x_change[i]

        # Enemy hitting the wall
        if enemy_x_pos[i] <= 0 or enemy_x_pos[i] >= 936:
            enemy_x_change[i] = -enemy_x_change[i]
            enemy_y_pos[i] += enemy_y_change[i]

        # Collision catch
        if enemy_icon[i].get_rect(x=enemy_x_pos[i], y=enemy_y_pos[i]).colliderect(bullet_icon.get_rect(x=bullet_x_pos, y=bullet_y_pos)):
            collision_sound = mixer.Sound("sounds/coins.mp3")
            collision_sound.play()

            bullet_y_pos = 480
            bullet_state = "ready"
            score_value += 1
            # Change enemy position
            enemy_x_pos[i] = random.randint(0, 936)
            enemy_y_pos[i] = random.randint(50, 200)


        enemy(enemy_x_pos[i], enemy_y_pos[i], i)

    # Bullet Movement 
    if bullet_y_pos <= 0:
        bullet_y_pos = 480
        bullet_state = "ready"

    if bullet_state == "fired":
        fire_bullet(bullet_x_pos,  bullet_y_pos)
        bullet_y_pos -= bullet_y_change

    player(player_x_pos, player_y_pos)
    show_score(text_x_pos, text_y_pos)
    pygame.display.update()


# Icons
# <a href="https://www.flaticon.com/free-icons/money" title="money icons">Money icons created by Chanut-is-Industries - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/machine-gun" title="machine gun icons">Machine gun icons created by Freepik - Flaticon</a>
# <a href="https://www.flaticon.com/free-icons/bank" title="bank icons">Bank icons created by Those Icons - Flaticon</a>
