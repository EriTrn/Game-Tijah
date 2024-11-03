import pygame
import random
from utils.helpers import determine_winner
from config.settings import WHITE, BLACK, ASSET_PATHS

def game_loop(screen, WIDTH, HEIGHT, WIDTH_SCALE, HEIGHT_SCALE):
    # Menggunakan font dengan skala yang lebih besar agar terlihat lebih jelas
    font = pygame.font.Font(None, int(30 * HEIGHT_SCALE))
    button_font = pygame.font.Font(None, int(36 * HEIGHT_SCALE))
    
    choices = ['Gajah', 'Jerapah', 'Semut']

    # Load gambar aset dengan ukuran yang disesuaikan
    gajah_img = pygame.image.load(ASSET_PATHS['gajah']).convert_alpha()
    jerapah_img = pygame.image.load(ASSET_PATHS['jerapah']).convert_alpha()
    semut_img = pygame.image.load(ASSET_PATHS['semut']).convert_alpha()

    # Menyesuaikan ukuran gambar agar sesuai dengan skala layar
    gajah_img = pygame.transform.scale(gajah_img, (int(80 * WIDTH_SCALE), int(90 * HEIGHT_SCALE)))
    jerapah_img = pygame.transform.scale(jerapah_img, (int(80 * WIDTH_SCALE), int(90 * HEIGHT_SCALE)))
    semut_img = pygame.transform.scale(semut_img, (int(80 * WIDTH_SCALE), int(90 * HEIGHT_SCALE)))

    # Posisi tombol pilihan permainan yang diskalakan
    button_width, button_height = int(100 * WIDTH_SCALE), int(40 * HEIGHT_SCALE)
    button_pos = {
        'Gajah': (int(80 * WIDTH_SCALE), int(260 * HEIGHT_SCALE)),
        'Jerapah': (int(240 * WIDTH_SCALE), int(260 * HEIGHT_SCALE)),
        'Semut': (int(400 * WIDTH_SCALE), int(260 * HEIGHT_SCALE)),
    }
    continue_button_pos = (int(140 * WIDTH_SCALE), int(320 * HEIGHT_SCALE))
    exit_button_pos = (int(350 * WIDTH_SCALE), int(320 * HEIGHT_SCALE))

    result = ""
    player_choice = ""
    computer_choice = ""
    round_over = False

    while True:
        screen.fill(WHITE)
        
        # Instruksi permainan
        instructions = font.render("Pilih: Gajah, Jerapah, atau Semut", True, BLACK)
        screen.blit(instructions, (int(150 * WIDTH_SCALE), int(50 * HEIGHT_SCALE)))

        # Menampilkan gambar pilihan yang diskalakan
        screen.blit(gajah_img, (int(100 * WIDTH_SCALE), int(100 * HEIGHT_SCALE)))
        screen.blit(jerapah_img, (int(240 * WIDTH_SCALE), int(100 * HEIGHT_SCALE)))
        screen.blit(semut_img, (int(400 * WIDTH_SCALE), int(100 * HEIGHT_SCALE)))

        # Menampilkan tombol pilihan
        for choice, pos in button_pos.items():
            pygame.draw.rect(screen, BLACK, (*pos, button_width, button_height), 2)
            text = button_font.render(choice, True, BLACK)
            screen.blit(text, (pos[0] + (button_width - text.get_width()) // 2, pos[1] + (button_height - text.get_height()) // 2))

        # Menampilkan hasil ronde
        if result:
            result_text = font.render(f"Player: {player_choice}, Computer: {computer_choice} - {result}", True, BLACK)
            screen.blit(result_text, (int(50 * WIDTH_SCALE), int(200 * HEIGHT_SCALE)))

        # Menampilkan opsi Lanjut dan Keluar jika ronde selesai
        if round_over:
            pygame.draw.rect(screen, BLACK, (*continue_button_pos, button_width, button_height), 2)
            pygame.draw.rect(screen, BLACK, (*exit_button_pos, button_width, button_height), 2)
            
            continue_text = button_font.render("Lanjut", True, BLACK)
            exit_text = button_font.render("Keluar", True, BLACK)

            screen.blit(continue_text, (continue_button_pos[0] + (button_width - continue_text.get_width()) // 2, continue_button_pos[1] + (button_height - continue_text.get_height()) // 2))
            screen.blit(exit_text, (exit_button_pos[0] + (button_width - exit_text.get_width()) // 2, exit_button_pos[1] + (button_height - exit_text.get_height()) // 2))

        # Event handling untuk input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # Jika ronde selesai, pilih antara Lanjut atau Keluar
                if round_over:
                    if continue_button_pos[0] < mouse_x < continue_button_pos[0] + button_width and \
                       continue_button_pos[1] < mouse_y < continue_button_pos[1] + button_height:
                        result = ""
                        round_over = False
                    elif exit_button_pos[0] < mouse_x < exit_button_pos[0] + button_width and \
                         exit_button_pos[1] < mouse_y < exit_button_pos[1] + button_height:
                        return 'menu'

                # Memilih pilihan permainan jika ronde belum selesai
                elif not round_over:
                    for choice, pos in button_pos.items():
                        if pos[0] < mouse_x < pos[0] + button_width and pos[1] < mouse_y < pos[1] + button_height:
                            player_choice = choice
                            computer_choice = random.choice(choices)
                            result = determine_winner(player_choice, computer_choice)
                            round_over = True

        pygame.display.flip()



