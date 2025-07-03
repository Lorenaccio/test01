import pygame
import math
import random

pygame.init()

# Taille de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chambre à 6 murs")

# Couleurs
WHITE = (255, 255, 255)
WALL_COLOR = (0, 0, 0)
BED_COLOR = (0, 0, 255)

# Fonction pour générer un hexagone régulier
def hexagon(center, radius):
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30  # rotation pour avoir un côté plat en bas
        angle_rad = math.radians(angle_deg)
        x = center[0] + radius * math.cos(angle_rad)
        y = center[1] + radius * math.sin(angle_rad)
        points.append((x, y))
    return points

# Coordonnées de l'hexagone
center = (WIDTH // 2, HEIGHT // 2)
radius = 200
hex_points = hexagon(center, radius)

# Créer un lit (rectangle bleu) à l'intérieur
# Le lit fera entre 150px et 350px de large
bed_width = random.randint(150, 350)
bed_height = 50
bed_x = center[0] - bed_width // 2
bed_y = center[1] - bed_height // 2
bed_rect = pygame.Rect(bed_x, bed_y, bed_width, bed_height)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Dessiner les murs (hexagone)
    pygame.draw.polygon(screen, WALL_COLOR, hex_points, width=5)

    # Dessiner le lit
    pygame.draw.rect(screen, BED_COLOR, bed_rect)

    pygame.display.flip()

pygame.quit()
