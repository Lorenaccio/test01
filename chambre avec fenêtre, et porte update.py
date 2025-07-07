import pygame
import random
from shapely.geometry import Polygon, box, LineString

# Initialisation
pygame.init()

# Constantes
SCALE = 50
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
WALL_COLOR = (100, 100, 100)
DOOR_COLOR = (0, 150, 0)
WINDOW_COLOR = (0, 180, 255)
BED_COLOR = (180, 0, 0)
TEXT_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chambre en L avec lit, porte et fenêtre")
clock = pygame.time.Clock()

# Police pour les légendes
font = pygame.font.SysFont("Arial", 16)

# Points en mètres pour une pièce en L
points_m = [
    (0, 0),
    (4, 0),
    (4, 2),
    (6, 2),
    (6, 5),
    (0, 5)
]

# Conversion
points_px = [(x * SCALE, y * SCALE) for x, y in points_m]
offset_x = (WINDOW_WIDTH - max(x for x, y in points_px)) // 2
offset_y = (WINDOW_HEIGHT - max(y for x, y in points_px)) // 2
points_px = [(x + offset_x, y + offset_y) for x, y in points_px]
polygon = Polygon(points_px)

# Définir les murs comme segments
walls = list(zip(points_px, points_px[1:] + [points_px[0]]))

# Choisir deux murs différents pour porte et fenêtre
door_wall = random.choice(walls)
window_wall = random.choice([w for w in walls if w != door_wall])

# Objets shapely pour la porte et fenêtre
def get_center_line(wall):
    (x1, y1), (x2, y2) = wall
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    if x1 == x2:  # vertical
        return LineString([(x1 - 5, mid_y - 30), (x1 + 5, mid_y + 30)])
    else:  # horizontal
        return LineString([(mid_x - 30, y1 - 5), (mid_x + 30, y1 + 5)])

door_shape = get_center_line(door_wall).buffer(5)
window_shape = get_center_line(window_wall).buffer(5)

# Placer le lit dans un endroit libre
bed_w_px = int(0.9 * SCALE)
bed_h_px = int(2.0 * SCALE)
bed_rect = None

for _ in range(500):
    x = random.randint(offset_x, offset_x + 600)
    y = random.randint(offset_y, offset_y + 400)
    candidate = box(x, y, x + bed_w_px, y + bed_h_px)

    if polygon.contains(candidate) and not candidate.intersects(door_shape) and not candidate.intersects(window_shape):
        bed_rect = pygame.Rect(x, y, bed_w_px, bed_h_px)
        break

# Fonction pour dessiner un élément sur un mur
def draw_on_wall(wall, color):
    line = get_center_line(wall)
    pygame.draw.line(screen, color, line.coords[0], line.coords[1], 8)

# Fonction pour dessiner une légende
def draw_legend(x, y, color, label):
    pygame.draw.rect(screen, color, (x, y, 20, 20))
    text = font.render(label, True, TEXT_COLOR)
    screen.blit(text, (x + 30, y + 2))

# Boucle principale
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessin de la pièce
    pygame.draw.polygon(screen, WALL_COLOR, points_px, 5)
    draw_on_wall(door_wall, DOOR_COLOR)
    draw_on_wall(window_wall, WINDOW_COLOR)

    if bed_rect:
        pygame.draw.rect(screen, BED_COLOR, bed_rect)

    # Légendes
    legend_start_x = 20
    legend_start_y = 20
    spacing = 30
    draw_legend(legend_start_x, legend_start_y + spacing * 0, WALL_COLOR, "Mur")
    draw_legend(legend_start_x, legend_start_y + spacing * 1, DOOR_COLOR, "Porte")
    draw_legend(legend_start_x, legend_start_y + spacing * 2, WINDOW_COLOR, "Fenêtre")
    draw_legend(legend_start_x, legend_start_y + spacing * 3, BED_COLOR, "Lit")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
