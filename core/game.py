import logging
from core.deck import Deck
from core.player import Player
from core.utils import log_action, VALID_INPUT_PATTERN

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()

    @log_action
    def compare_cards(self, house_card, player_card, guess):
        if guess.lower() not in ['greater', 'less']:
            raise ValueError("Invalid guess.")
        result = player_card.value > house_card.value
        if guess.lower() == 'less':
            result = not result
        return result

    def play_round(self):
        try:
            self.player.pay_to_play()
        except ValueError as e:
            print(e)
            return False

        house_card = self.deck.draw()
        logging.info(f"House drew card: {house_card}")
        print(f"House's card: {house_card}")

        guess = input("Is your card 'greater' or 'less' than the house's card? ").strip()
        while not VALID_INPUT_PATTERN.match(guess):
            guess = input("Invalid input. Enter 'greater' or 'less': ").strip()

        logging.info(f"Player guessed: {guess}")

        player_card = self.deck.draw()
        logging.info(f"Player drew card: {player_card}")
        print(f"Your card: {player_card}")

        try:
            if self.compare_cards(house_card, player_card, guess):
                print("You won this round!")
                logging.info("Result: Player won.")
                self.player.win()
                return True
            else:
                print("You lost this round.")
                logging.info("Result: Player lost.")
                self.player.lose()
                return False
        except Exception as e:
            logging.error(f"Error comparing cards: {e}")
            print("Error:", e)
            return False

    def start(self):
        logging.info("Game started.")

        while True:
            print(f"Current points: {self.player.points}")
            logging.info(f"Current points: {self.player.points}")

            if self.player.points < 30:
                print("You LOST the game!")
                logging.info("Game over: player lost.")
                break

            if self.player.points >= 100:
                print("Congratulations! You WON the game!")
                logging.info("Game over: player won.")
                break

            won = self.play_round()

            if won:
                choice = input("Do you want to continue and double the reward? (yes/no): ").strip().lower()
                logging.info(f"Player chose to {'continue' if choice == 'yes' else 'claim reward'}.")

                if choice == "no":
                    self.player.claim_reward()
                    print(f"Reward claimed. Points: {self.player.points}")
                    logging.info(f"Points after claiming reward: {self.player.points}")
            else:
                print("No reward this round.")
