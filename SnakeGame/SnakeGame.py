import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.add_block()

    def add_block(self):
        self.body.append((0, 0))

    def move(self):
        head = self.body[0]
        x, y = head
        if self.direction == "UP":
            y -= 1
        elif self.direction == "DOWN":
            y += 1
        elif self.direction == "LEFT":
            x -= 1
        elif self.direction == "RIGHT":
            x += 1
        self.body = [(x, y)] + self.body[:-1]

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def draw(self):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Food
class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def draw(self):
        x, y = self.position
        pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Main game loop
def main():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        snake.move()

        # Check for collision with food
        if snake.body[0] == food.position:
            snake.add_block()
            food.position = food.generate_position()

        # Check for collision with the walls
        head_x, head_y = snake.body[0]
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            running = False

        # Check for collision with itself
        if len(snake.body) != len(set(snake.body)):
            running = False

        snake.draw()
        food.draw()

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
