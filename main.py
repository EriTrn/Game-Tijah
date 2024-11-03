from core.menu import show_main_menu
from core.game import game_loop
import pygame
from config.settings import BASE_WIDTH, BASE_HEIGHT

def main():
    pygame.init()
    
    # Setup layar sementara
    screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT))
    pygame.display.set_caption("Game Tijah - Jempol Telunjuk Kelingking")

    # Mendapatkan ukuran layar perangkat
    screen_info = pygame.display.Info()
    device_width, device_height = screen_info.current_w, screen_info.current_h

    # Faktor skala berdasarkan ukuran perangkat saat ini
    WIDTH_SCALE = device_width / BASE_WIDTH
    HEIGHT_SCALE = device_height / BASE_HEIGHT

    # Hitung ukuran layar berdasarkan skala
    WIDTH = int(BASE_WIDTH * WIDTH_SCALE)
    HEIGHT = int(BASE_HEIGHT * HEIGHT_SCALE)

    # Set layar dengan ukuran disesuaikan
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # Loop utama untuk mengelola menu dan permainan
    running = True
    mode = 'menu'

    while running:
        if mode == 'menu':
            mode = show_main_menu(screen, WIDTH, HEIGHT, WIDTH_SCALE, HEIGHT_SCALE)
        elif mode == 'game':
            mode = game_loop(screen, WIDTH, HEIGHT, WIDTH_SCALE, HEIGHT_SCALE)
        else:
            running = False  # Exit jika mode bukan menu atau game

    pygame.quit()

if __name__ == "__main__":
    main()

