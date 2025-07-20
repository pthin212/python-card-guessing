import logging
from core.utils import reward_multiplier

class Player:
    def __init__(self):
        self._points = 60
        self._reward = 0
        self.multiplier = reward_multiplier()

    @property
    def points(self):
        return self._points

    def pay_to_play(self):
        if self._points < 25:
            logging.info("Player tried to play with insufficient points.")
            raise ValueError("Not enough points to play.")
        self._points -= 25
        logging.info(f"Player paid 25 points to play. Remaining: {self._points}")
        print(f"25 points deducted to join the match. Remaining points: {self._points}")

    def win(self):
        reward = self.multiplier()
        self._reward = reward
        logging.info(f"Player won the round. Current reward: {reward}")

    def lose(self):
        logging.info("Player lost the round.")
        self._reward = 0
        self.multiplier = reward_multiplier()

    def claim_reward(self):
        logging.info(f"Player claimed reward of {self._reward} points.")
        self._points += self._reward
        self._reward = 0
        self.multiplier = reward_multiplier()
