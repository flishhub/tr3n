import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tr3n Light Cycle")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 36)

# Colors
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Game states
MENU, PLAYING, GAME_OVER = "menu", "playing", "game_over"
state = MENU

# Light Cycle class
class LightCycle:
    def __init__(self, x, y, color, keys):
        self.x = x
        self.y = y
        self.color = color
        self.dir = "RIGHT"
        self.speed = 5
        self.trail = []
        self.keys = keys

    def move(self):
        if self.dir == "UP":
            self.y -= self.speed
        elif self.dir == "DOWN":
            self.y += self.speed
        elif self.dir == "LEFT":
            self.x -= self.speed
        elif self.dir == "RIGHT":
            self.x += self.speed
        self.trail.append((self.x, self.y))

    def draw(self):
        for pos in self.trail:
            pygame.draw.rect(SCREEN, self.color, (*pos, 5, 5))

    def check_collision(self):
        return (self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT or (self.x, self.y) in self.trail[:-10])

def draw_menu():
    SCREEN.fill(BLACK)
    title = FONT.render("Tr3n Light Cycle", True, CYAN)
    start = FONT.render("Press ENTER to Start", True, WHITE)
    quit = FONT.render("Press ESC to Quit", True, WHITE)
    SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, 150))
    SCREEN.blit(start, (WIDTH//2 - start.get_width()//2, 250))
    SCREEN.blit(quit, (WIDTH//2 - quit.get_width()//2, 300))
    pygame.display.flip()

def draw_game_over():
    SCREEN.fill(BLACK)
    msg = FONT.render("Game Over!", True, RED)
    restart = FONT.render("Press ENTER to Restart", True, WHITE)
    SCREEN.blit(msg, (WIDTH//2 - msg.get_width()//2, 200))
    SCREEN.blit(restart, (WIDTH//2 - restart.get_width()//2, 300))
    pygame.display.flip()

# Main loop
cycle = LightCycle(100, 100, CYAN, {"UP": pygame.K_w, "DOWN": pygame.K_s, "LEFT": pygame.K_a, "RIGHT": pygame.K_d})

while True:
    CLOCK.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if state == MENU:
        draw_menu()
        if keys[pygame.K_RETURN]:
            cycle = LightCycle(100, 100, CYAN, {"UP": pygame.K_w, "DOWN": pygame.K_s, "LEFT": pygame.K_a, "RIGHT": pygame.K_d})
            state = PLAYING
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    elif state == PLAYING:
        SCREEN.fill(BLACK)
        if keys[cycle.keys["UP"]]:
            cycle.dir = "UP"
        elif keys[cycle.keys["DOWN"]]:
            cycle.dir = "DOWN"
        elif keys[cycle.keys["LEFT"]]:
            cycle.dir = "LEFT"
        elif keys[cycle.keys["RIGHT"]]:
            cycle.dir = "RIGHT"

        cycle.move()
        cycle.draw()

        if cycle.check_collision():
            state = GAME_OVER

        pygame.display.flip()

    elif state == GAME_OVER:
        draw_game_over()
        if keys[pygame.K_RETURN]:
            state = MENU