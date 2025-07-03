import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pièce avec meuble")

# Couleurs
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BED_COLOR = (0, 0, 255)  # bleu pour le "lit"
WALL_COLOR = (0, 0, 0)

# Échelle : 1 mètre = 50 pixels
METER = 50
MIN_WIDTH = 3 * METER
MAX_WIDTH = 7 * METER

# Générer la pièce
room_margin = 100
room_rect = pygame.Rect(room_margin, room_margin, SCREEN_WIDTH - 2*room_margin, SCREEN_HEIGHT - 2*room_margin)

# Générer un lit avec largeur entre 3 et 7m
bed_width = random.randint(MIN_WIDTH, MAX_WIDTH)
bed_height = METER  # 1m de hauteur
bed_x = random.randint(room_rect.left, room_rect.right - bed_width)
bed_y = random.randint(room_rect.top, room_rect.bottom - bed_height)
bed_rect = pygame.Rect(bed_x, bed_y, bed_width, bed_height)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Dessiner les murs (bords de la pièce)
    pygame.draw.rect(screen, WALL_COLOR, room_rect, 5)

    # Dessiner le lit
    pygame.draw.rect(screen, BED_COLOR, bed_rect)

    pygame.display.flip()

pygame.quit()

