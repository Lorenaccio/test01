import pygame
import math
import random

pygame.init()

# Taille de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chambre à 6 murs avec porte et fenêtre")

# Couleurs
WHITE = (255, 255, 255)
WALL_COLOR = (0, 0, 0)
BED_COLOR = (0, 0, 255)
DOOR_COLOR = (139, 69, 19)      # marron
WINDOW_COLOR = (135, 206, 250)  # bleu clair

# Fonctions
def hexagon(center, radius):
    """Retourne les points d'un hexagone régulier"""
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.radians(angle_deg)
        x = center[0] + radius * math.cos(angle_rad)
        y = center[1] + radius * math.sin(angle_rad)
        points.append((x, y))
    return points

def midpoint(p1, p2):
    """Retourne le point milieu entre deux points"""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Centre et taille
center = (WIDTH // 2, HEIGHT // 2)
radius = 200
hex_points = hexagon(center, radius)

# Choisir deux murs différents pour la porte et la fenêtre
wall_indices = list(range(6))
door_wall = random.choice(wall_indices)
wall_indices.remove(door_wall)
window_wall = random.choice(wall_indices)

# Coordonnées de la porte et fenêtre (milieu des segments)
door_pos = midpoint(hex_points[door_wall], hex_points[(door_wall + 1) % 6])
window_pos = midpoint(hex_points[window_wall], hex_points[(window_wall + 1) % 6])

# Taille visuelle
opening_width = 40
opening_height = 10

# Créer un lit centré
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
    for i in range(6):
        p1 = hex_points[i]
        p2 = hex_points[(i + 1) % 6]

        # Ne pas dessiner la portion centrale du mur avec porte ou fenêtre
        mid = midpoint(p1, p2)
        vec = ((p2[0] - p1[0]), (p2[1] - p1[1]))
        length = math.hypot(*vec)
        unit_vec = (vec[0] / length, vec[1] / length)
        offset = opening_width / 2

        # Points avant et après l'ouverture
        before = (mid[0] - unit_vec[0] * offset, mid[1] - unit_vec[1] * offset)
        after = (mid[0] + unit_vec[0] * offset, mid[1] + unit_vec[1] * offset)

        if i == door_wall or i == window_wall:
            # Découpe le mur : p1 -> before, after -> p2
            pygame.draw.line(screen, WALL_COLOR, p1, before, 5)
            pygame.draw.line(screen, WALL_COLOR, after, p2, 5)
        else:
            pygame.draw.line(screen, WALL_COLOR, p1, p2, 5)

    # Dessiner la porte
    pygame.draw.circle(screen, DOOR_COLOR, (int(door_pos[0]), int(door_pos[1])), 8)

    # Dessiner la fenêtre
    pygame.draw.rect(screen, WINDOW_COLOR,
                     pygame.Rect(window_pos[0] - 10, window_pos[1] - 10, 20, 20))

    # Dessiner le lit
    pygame.draw.rect(screen, BED_COLOR, bed_rect)

    pygame.display.flip()

pygame.quit()
