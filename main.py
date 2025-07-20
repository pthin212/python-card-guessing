from core.game import Game
from config.logger import log_filename

if __name__ == "__main__":
    print(f"Logging to file: {log_filename}")
    game = Game()
    game.start()