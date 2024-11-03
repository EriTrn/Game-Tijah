import pygame
from config.settings import WHITE, BLACK, GREEN, RED

def show_main_menu(screen, WIDTH, HEIGHT, WIDTH_SCALE, HEIGHT_SCALE):
    font = pygame.font.Font(None, int(48 * HEIGHT_SCALE))
    small_font = pygame.font.Font(None, int(36 * HEIGHT_SCALE))
    title_y = HEIGHT // 2 - int(100 * HEIGHT_SCALE)

    while True:
        screen.fill(WHITE)
        title_text = font.render("Game Tijah", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, title_y))

        if title_y > int(100 * HEIGHT_SCALE):
            title_y -= 2

        start_button = pygame.Rect(WIDTH // 2 - int(100 * WIDTH_SCALE), int(200 * HEIGHT_SCALE), int(200 * WIDTH_SCALE), int(50 * HEIGHT_SCALE))
        quit_button = pygame.Rect(WIDTH // 2 - int(100 * WIDTH_SCALE), int(270 * HEIGHT_SCALE), int(200 * WIDTH_SCALE), int(50 * HEIGHT_SCALE))
        
        pygame.draw.rect(screen, GREEN, start_button)
        pygame.draw.rect(screen, RED, quit_button)
        
        screen.blit(small_font.render("Mulai", True, BLACK), (start_button.x + int(60 * WIDTH_SCALE), start_button.y + int(10 * HEIGHT_SCALE)))
        screen.blit(small_font.render("Quit Game", True, BLACK), (quit_button.x + int(35 * WIDTH_SCALE), quit_button.y + int(10 * HEIGHT_SCALE)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return 'game'
                elif quit_button.collidepoint(event.pos):
                    return 'exit'
                    
        pygame.display.flip()
