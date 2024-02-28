import pygame
from colorama import Fore, Style

def play_music(file_name):
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()

        print(Fore.YELLOW + f"Memutar file: {file_name}")
        print(Fore.GREEN + "Tekan 'q' untuk berhenti")
        
        while pygame.mixer.music.get_busy():
            user_input = input()
            if user_input == 'q':
                pygame.mixer.music.stop()
                break
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
    finally:
        pygame.quit()
        print(Style.RESET_ALL + "Aplikasi telah ditutup")

if __name__ == "__main__":
    file_name = "Seventeen - My My [128 kbps].mp3"
    play_music(file_name)